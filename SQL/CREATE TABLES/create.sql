-- CREATE table with foreign keys

CREATE TABLE job_accounts (
    user_id INTEGER REFERENCES example1(user_id),
	job_id INTEGER REFERENCES jobs(job_id), 
	hire_date TIMESTAMP
)