-- create fact table "loan_fact"
CREATE TABLE loan_fact(
   loan_id integer,
   grade_id integer NOT NULL,
   term_id integer NOT NULL,
   initial_list_status_id integer NOT NULL,
   home_ownership_id integer NOT NULL,
   emp_title_id integer NOT NULL,
   verification_status_id integer NOT NULL,
   title_id integer NOT NULL,
   addr_state_id integer NOT NULL,
   loan_status_id integer NOT NULL,
   loan_amnt numeric,
   installment numeric ,
   annual_inc numeric,
   loan_income_ratio numeric,
   funded_amnt_inv numeric,
   sub_grade char (4),
   emp_length varchar,
   issue_d varchar,
   delinq_2yrs integer,
   earliest_cr_line date,
   inq_last_6mths integer,
   revol_bal integer,
   total_acc integer,
   total_pymnt numeric,
   total_rec_prncp numeric,
   total_rec_int numeric,
   last_pymnt_d date,
   last_pymnt_amnt numeric,
   last_credit_pull_d date,
   tot_coll_amt integer,
   open_acc_6m integer,
   open_act_il integer,
   open_il_12m integer,
   open_il_24m integer,
   mths_since_rcnt_il integer,
   total_bal_il integer,
   il_util integer,
   open_rv_12m integer,
   open_rv_24m integer,
   max_bal_bc integer,
   all_util integer,
   inq_fi integer,
   total_cu_tl integer,
   inq_last_12m integer,
   acc_open_past_24mths integer,
   avg_cur_bal integer,
   bc_open_to_buy integer,
   mo_sin_old_il_acct integer,
   mo_sin_old_rev_tl_op integer,
   mo_sin_rcnt_rev_tl_op integer,
   mo_sin_rcnt_tl integer,
   mort_acc integer,
   mths_since_recent_bc integer,
   mths_since_recent_inq integer,
   num_accts_ever_120_pd integer,
   num_il_tl integer,
   num_sats integer,
   num_tl_op_past_12m integer,
   pct_tl_nvr_dlq numeric,
   percent_bc_gt_75 numeric,
   total_bal_ex_mort integer,
   total_bc_limit integer,
   debt_settlement_flag char,
   loan_income_ratio numeric,
   issue_month integer,
   issue_year integer,
   id integer,
   primary key (id),
   FOREIGN KEY (grade_id) REFERENCES grade (grade_id),
   FOREIGN KEY (term_id) REFERENCES term (term_id),
   FOREIGN KEY (initial_list_status_id) REFERENCES initial_list_status (initial_list_status_id),
   FOREIGN KEY (home_ownership_id) REFERENCES home_ownership (home_ownership_id),
   FOREIGN KEY (loan_status_id) REFERENCES loan_status (loan_status_id),
   FOREIGN KEY (addr_state_id) REFERENCES addr_state (addr_state_id),
   FOREIGN KEY (title_id) REFERENCES title (title_id),
   FOREIGN KEY (emp_title_id) REFERENCES emp_title (emp_title_id),
   FOREIGN KEY (verification_status_id) REFERENCES verification_status (verification_status_id)
);


-- create dimensional table "grade"
CREATE TABLE grade(
   grade_id integer PRIMARY KEY,
   grade varchar,
   FOREIGN KEY (grade_id) REFERENCES loan_fact (grade_id)
);


-- create dimensional table "term"
CREATE TABLE term(
   term_id integer PRIMARY KEY,
   term varchar,
   FOREIGN KEY (term_id) REFERENCES loan_fact (term_id)
);


-- create dimensional table "initial_list_status"
CREATE TABLE initial_list_status(
   initial_list_status_id integer PRIMARY KEY,
   initial_list_status varchar,
   FOREIGN KEY (initial_list_status_id) REFERENCES loan_fact (initial_list_status_id)
);


-- create dimensional table "home_ownership"
CREATE TABLE home_ownership(
   home_ownership_id integer PRIMARY KEY,
   home_ownership varchar,
   FOREIGN KEY (home_ownership_id) REFERENCES loan_fact (home_ownership_id)
);


-- create dimensional table "loan_status"
CREATE TABLE loan_status(
   loan_status_id integer PRIMARY KEY,
   loan_status varchar,
   FOREIGN KEY (loan_status_id) REFERENCES loan_fact (loan_status_id)
);


-- create dimensional table "addr_state"
CREATE TABLE addr_state(
   addr_state_id integer PRIMARY KEY,
   addr_state varchar,
   FOREIGN KEY (addr_state_id) REFERENCES loan_fact (addr_state_id)
);


-- create dimensional table "title"
CREATE TABLE title(
   title_id integer PRIMARY KEY,
   title varchar,
   FOREIGN KEY (title_id) REFERENCES loan_fact (title_id)
);


-- create dimensional table "emp_title"
CREATE TABLE emp_title(
   emp_title_id integer PRIMARY KEY,
   emp_title varchar,
   FOREIGN KEY (emp_title_id) REFERENCES loan_fact (emp_title_id)
);

-- create dimensional table "verification_status"
CREATE TABLE verification_status(
   verification_status_id integer PRIMARY KEY,
   verification_status varchar,
   FOREIGN KEY (verification_status_id) REFERENCES loan_fact (verification_status_id)
);
