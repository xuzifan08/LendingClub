-- create fact table "loan_fact"
CREATE TABLE loan_fact(
   loan_id integer PRIMARY KEY,
   grade_id integer NOT NULL,
   term_id integer NOT NULL,
   initial_list_status_id integer NOT NULL,
   home_ownership_id integer NOT NULL,
   emp_title_id integer NOT NULL,
   verification_status_id integer NOT NULL,
   title_id integer NOT NULL,
   addr_state_id integer NOT NULL,
   loan_status_id integer NOT NULL,
   loan_amnt ??????,
   installment ????,
   annual_inc ??? ,
   loan_income_ratio ????,
   ...
);


-- create dimensional table "grade"
CREATE TABLE grade(
   grade_id integer PRIMARY KEY,
   grade ???,
);


-- create dimensional table "term"
CREATE TABLE term(
   term_id integer PRIMARY KEY,
   term ???,
);


-- create dimensional table "initial_list_status"
CREATE TABLE initial_list_status(
   initial_list_status_id integer PRIMARY KEY,
   initial_list_status ???,
);


-- create dimensional table "home_ownership"
CREATE TABLE home_ownership(
   home_ownership_id integer PRIMARY KEY,
   home_ownership ???,
);


-- create dimensional table "loan_status"
CREATE TABLE loan_status(
   loan_status_id integer PRIMARY KEY,
   loan_status ???,
);


-- create dimensional table "addr_state"
CREATE TABLE addr_state(
   addr_state_id integer PRIMARY KEY,
   addr_state ???,
);


-- create dimensional table "title"
CREATE TABLE title(
   title_id integer PRIMARY KEY,
   title ???,
);


-- create dimensional table "emp_title"
CREATE TABLE emp_title(
   emp_title_id integer PRIMARY KEY,
   emp_title ???,
);

