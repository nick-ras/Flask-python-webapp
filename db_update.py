from datetime import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import select, update
import pytz, time
import os


#ru nevery 15 minutes
# Function to run the update logic
class update_db():
	def update_box_script(self):
		engine = create_engine(os.getenv("DATABASE_URL"))
		metadata = MetaData()
		session = engine.connect()

		# Assuming 'boxes' is the table name
		boxes_table = Table('boxes', metadata, autoload_with=engine)
		# Get the current time in UTC
		#fixit get curr timezone SELECT CURRENT_TIMEZONE(), datetime.utcnow().replace(tzinfo=pytz.utc)
		current_time = engine.execute('SELECT CURRENT_TIMEZONE()')
		print(f"\ncurrent_time from db {current_time.fetchone()[0]}\n")
		# Build a query to select all rows where 'in_use' is True and 'booked_until_interval15' is in the past
		query = select(boxes_table).where(
				(boxes_table.c.in_use == True) &
				(boxes_table.c.booked_until_interval15 < current_time)
		)
		
		# Execute the query
		results = session.execute(query).fetchall()

		# Update the 'in_use' status for rows where 'booked_until_interval15' is in the past
		for row in results:
				update_query = update(boxes_table).where(boxes_table.c.id == row.id).values(in_use=False, booked_until_interval15=None, user_id=None)
				session.execute(update_query)
		
		# Commit the changes
		session.commit()
		session.close()

	# Run the update logic every 15 minutes
	def update_db_infinite(self):
		while (1):
			self.update_box_script()
			print("Updated box statuses in 15 minutes loop")
			time.sleep(900)