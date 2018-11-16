import datetime
from . import formatter
from app.database import database

date_format = '%Y-%m-%d %H:%M:%S'

def stop_active_sessions():
	database.execute("UPDATE training_sessions SET deactivated = 1 WHERE deactivated = 0 AND endTime IS NULL AND startTime IS NOT NULL")

def get_active_session():
	session = database.fetchone("SELECT * FROM training_sessions WHERE deactivated = 0 AND endTime IS NULL AND startTime IS NOT NULL LIMIT 1")

	if session:
		return formatter.format(session)

def create_new_session(session):
	inputs = (session['name'], session['episodeLimit'], session['secondsLimit'])

	return database.insert("INSERT INTO training_sessions (name, episodeLimit, secondsLimit) VALUES (?, ?, ?)", inputs)

def get_next_session():
	active_session = get_active_session()

	if active_session:
		return

	session = database.fetchone("SELECT * FROM training_sessions WHERE deactivated = 0 AND endTime IS NULL AND startTime IS NULL LIMIT 1")

	if session:
		return formatter.format(session)

def activate(id):
	time = datetime.datetime.now().strftime(date_format)

	database.execute("UPDATE training_sessions SET startTime = ? WHERE id = ?", (time, id))

def boost_episode_count(id, episodes):
	database.execute("UPDATE training_sessions SET episodeCount = episodeCount + ? WHERE id = ?", (episodes, id))

def is_active(id):
	return not not database.fetchone("SELECT id FROM training_sessions WHERE deactivated = 0 AND endTime IS NULL AND startTime IS NOT NULL")

def finish(id):
	time = datetime.datetime.now().strftime(date_format)

	database.execute("UPDATE training_sessions SET endTime = ? WHERE id = ?", (time, id))

def get_latest_session():
	session = database.fetchone("SELECT * FROM training_sessions WHERE episodeCount > 0 ORDER BY startTime DESC")

	if session:
		return formatter.format(session)

def get_all():
	result = database.fetchall("SELECT * FROM training_sessions ORDER BY createdAt DESC")

	return formatter.format_many(result)