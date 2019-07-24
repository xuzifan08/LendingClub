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
);


