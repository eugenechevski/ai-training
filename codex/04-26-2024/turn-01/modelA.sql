CREATE EVENT my_cleanup_event 
ON SCHEDULE EVERY 1 DAY  -- Adjust the interval as needed
DO
    DELETE FROM old_log_data 
    WHERE log_date < DATE_SUB(NOW(), INTERVAL 1 MONTH); 