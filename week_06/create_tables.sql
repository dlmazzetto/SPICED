CREATE TABLE shippers (
  shipper_id SERIAL PRIMARY KEY,
  company_name VARCHAR(100) NOT NULL,
  phone VARCHAR(15)
);

COPY shippers FROM '/Users/PaulWlodkowski/Documents/PythonWork/SPICED-Work/GIT_REPOS/Teaching/logistic-lemongrass/logistic-lemongrass-encounter-notes/week_06/northwind_data_clean/data/shippers.csv' DELIMITER ',' CSV HEADER;

-- for windows, you need to write \copy
