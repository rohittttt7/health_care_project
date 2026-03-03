-- overview
select * from patient;

-- total patients
select count(*)as total_patients from patient;


-- average risk score & stay

select round(avg(risk_score))as avg_risk,
	   round(avg(lengthofstay))as avg_stay
	   from patient;

-- CONDITION-BASED ANALYSIS

-- risk & stay by medical condition

select medical_condition,count(*)as total_patient,
round(avg(risk_score))as avg_risk,
round(avg(lengthofstay))as avg_stay
	   from patient
group by medical_condition
order by avg_risk desc;

-- LIFESTYLE IMPACT ANALYSIS

-- smoking impact

select smoking,
avg(cholesterol) as avg_cholesterol,
avg(risk_score) as avg_risk
from patient
group by smoking;

-- alcohol impact

select alcohol,
round(avg(risk_score))as avg_risk,
round(avg(lengthofstay))as avg_stay
from patient
group by alcohol

-- STRESS & SLEEP ANALYSIS

-- Stress Category vs Sleep

select 
	case
		when stress_level<3 then 'low'
		when stress_level<6 then 'median'
		when stress_level<9 then 'high'
		else 'very-high'
	end as stress_category,
	avg(sleep_hours)as avg_sleep
from patient
group by stress_category
order by avg_sleep desc;

--      BMI CATEGORY ANALYSIS

-- BMI Category vs Stay

select bmi_category,
count(*)as total_people,
avg(lengthofstay) as avg_stay,
avg(risk_score) as avg_risk
from patient
group by bmi_category
order by avg_risk desc


-- Rank Medical Conditions by Risk

select medical_condition,
round(avg(risk_score))as avg_risk,
rank()over(order by avg(risk_score)desc) as risk_rank
from patient
group by medical_condition;


-- Top 10 High-Risk Patients per Condition

select * from(
select *,row_number() over(
partition by medical_condition
order by risk_score desc)as rn
from patient
)sub
where rn<=10;

-- risk segmentation

select case 
			when  risk_score <150 then 'low'
			when  risk_score<250 then 'medium'
			else 'high'
		end as risk_category,
		count(*) as total_people,
		(avg(lengthofstay)) as avg_stay
from patient 
group by risk_category
order by avg_stay desc;

-- CORRELATION-LIKE TREND ANALYSIS

-- Does Physical Activity Reduce Risk?

select 
avg(physical_activity) as avg_activity,
avg(risk_score) as avg_risk
from patient

-- bucket activity:
select case
when physical_activity <3 then 'low activity'
when physical_activity<6 then 'medium activity'
else 'high activity'
end as activity_level,
avg(risk_score) as avg_risk
from patient
group by activity_level
order by avg_risk desc;

-- EXECUTIVE SUMMARY QUERY

select count(*) as total_patient,
avg(risk_score) as avg_risk,
avg(lengthofstay)as avg_stay,
avg(bmi) as avg_bmi,
avg(cholesterol)as avg_cholesterol
from patient



