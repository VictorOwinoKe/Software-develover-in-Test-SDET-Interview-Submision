
use task_manager;

--Total number of tasks in the database

SELECT COUNT(DISTINCT task_id) AS Total_tasks
FROM task;

--Number of completed tasks
SELECT COUNT(DISTINCT task_id) AS Completed_tasks
FROM tasks
WHERE task_completed = 1; --  '1' represents completed tasks

--Number of tasks assigned to each unique user:
SELECT task_assignee, COUNT(DISTINCT task_id) AS Total_assigned_tasks
FROM tasks
GROUP BY task_assignee;
 
 --##Justification for use of this script
 --This SQL script can be very essential in verufying application behaviour such as;
   --Verify that the applications creates tasks correctly as espected.
   --Verify that the applications assignes tasks correctly to the users.
   --Verify that the completion status of tasks is updated accurately.

