-- ============================================================================
-- Hotel Booking EDA - Basic Analysis
-- Purpose: Exploratory data analysis using CTEs for hotel booking data
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 1. BOOKING OVERVIEW
-- ----------------------------------------------------------------------------
WITH booking_overview AS (
    SELECT 
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS total_canceled,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate,
        ROUND(AVG(lead_time), 2) AS avg_lead_time,
        ROUND(AVG(adr), 2) AS avg_daily_rate,
        ROUND(AVG(stays_in_weekend_nights + stays_in_week_nights), 2) AS avg_nights
    FROM hotel_bookings
)
SELECT * FROM booking_overview;


-- ----------------------------------------------------------------------------
-- 2. CANCELLATION BY HOTEL TYPE
-- ----------------------------------------------------------------------------
WITH cancellation_by_hotel AS (
    SELECT 
        hotel,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate
    FROM hotel_bookings
    GROUP BY hotel
)
SELECT * FROM cancellation_by_hotel
ORDER BY cancellation_rate DESC;


-- ----------------------------------------------------------------------------
-- 3. MONTHLY BOOKING TRENDS
-- ----------------------------------------------------------------------------
WITH monthly_trends AS (
    SELECT 
        arrival_date_month AS month,
        arrival_date_year AS year,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate
    FROM hotel_bookings
    GROUP BY arrival_date_month, arrival_date_year
)
SELECT * FROM monthly_trends
ORDER BY year, 
    CASE month
        WHEN 'January' THEN 1
        WHEN 'February' THEN 2
        WHEN 'March' THEN 3
        WHEN 'April' THEN 4
        WHEN 'May' THEN 5
        WHEN 'June' THEN 6
        WHEN 'July' THEN 7
        WHEN 'August' THEN 8
        WHEN 'September' THEN 9
        WHEN 'October' THEN 10
        WHEN 'November' THEN 11
        WHEN 'December' THEN 12
    END;


-- ----------------------------------------------------------------------------
-- 4. MARKET SEGMENT ANALYSIS
-- ----------------------------------------------------------------------------
WITH market_analysis AS (
    SELECT 
        market_segment,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate,
        ROUND(AVG(adr), 2) AS avg_daily_rate
    FROM hotel_bookings
    GROUP BY market_segment
)
SELECT * FROM market_analysis
ORDER BY total_bookings DESC;


-- ----------------------------------------------------------------------------
-- 5. LEAD TIME IMPACT ON CANCELLATION
-- ----------------------------------------------------------------------------
WITH lead_time_analysis AS (
    SELECT 
        CASE 
            WHEN lead_time = 0 THEN 'Same Day'
            WHEN lead_time BETWEEN 1 AND 7 THEN '1-7 Days'
            WHEN lead_time BETWEEN 8 AND 30 THEN '1-4 Weeks'
            WHEN lead_time BETWEEN 31 AND 90 THEN '1-3 Months'
            WHEN lead_time BETWEEN 91 AND 180 THEN '3-6 Months'
            ELSE '6+ Months'
        END AS lead_time_category,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate
    FROM hotel_bookings
    GROUP BY 
        CASE 
            WHEN lead_time = 0 THEN 'Same Day'
            WHEN lead_time BETWEEN 1 AND 7 THEN '1-7 Days'
            WHEN lead_time BETWEEN 8 AND 30 THEN '1-4 Weeks'
            WHEN lead_time BETWEEN 31 AND 90 THEN '1-3 Months'
            WHEN lead_time BETWEEN 91 AND 180 THEN '3-6 Months'
            ELSE '6+ Months'
        END
)
SELECT * FROM lead_time_analysis
ORDER BY 
    CASE lead_time_category
        WHEN 'Same Day' THEN 1
        WHEN '1-7 Days' THEN 2
        WHEN '1-4 Weeks' THEN 3
        WHEN '1-3 Months' THEN 4
        WHEN '3-6 Months' THEN 5
        WHEN '6+ Months' THEN 6
    END;


-- ----------------------------------------------------------------------------
-- 6. CUSTOMER TYPE BEHAVIOR
-- ----------------------------------------------------------------------------
WITH customer_behavior AS (
    SELECT 
        customer_type,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate,
        ROUND(AVG(stays_in_weekend_nights + stays_in_week_nights), 2) AS avg_nights,
        ROUND(AVG(adr), 2) AS avg_daily_rate
    FROM hotel_bookings
    GROUP BY customer_type
)
SELECT * FROM customer_behavior
ORDER BY total_bookings DESC;


-- ----------------------------------------------------------------------------
-- 7. SPECIAL REQUESTS IMPACT
-- ----------------------------------------------------------------------------
WITH special_requests_impact AS (
    SELECT 
        CASE 
            WHEN total_of_special_requests = 0 THEN 'No Requests'
            WHEN total_of_special_requests = 1 THEN '1 Request'
            WHEN total_of_special_requests = 2 THEN '2 Requests'
            ELSE '3+ Requests'
        END AS request_category,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate
    FROM hotel_bookings
    GROUP BY 
        CASE 
            WHEN total_of_special_requests = 0 THEN 'No Requests'
            WHEN total_of_special_requests = 1 THEN '1 Request'
            WHEN total_of_special_requests = 2 THEN '2 Requests'
            ELSE '3+ Requests'
        END
)
SELECT * FROM special_requests_impact
ORDER BY 
    CASE request_category
        WHEN 'No Requests' THEN 1
        WHEN '1 Request' THEN 2
        WHEN '2 Requests' THEN 3
        WHEN '3+ Requests' THEN 4
    END;


-- ----------------------------------------------------------------------------
-- 8. REPEATED GUEST ANALYSIS
-- ----------------------------------------------------------------------------
WITH repeated_guest_analysis AS (
    SELECT 
        CASE WHEN is_repeated_guest = 1 THEN 'Repeated Guest' ELSE 'New Guest' END AS guest_type,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate,
        ROUND(AVG(adr), 2) AS avg_daily_rate
    FROM hotel_bookings
    GROUP BY is_repeated_guest
)
SELECT * FROM repeated_guest_analysis;


-- ----------------------------------------------------------------------------
-- 9. DEPOSIT TYPE IMPACT
-- ----------------------------------------------------------------------------
WITH deposit_analysis AS (
    SELECT 
        deposit_type,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate
    FROM hotel_bookings
    GROUP BY deposit_type
)
SELECT * FROM deposit_analysis
ORDER BY cancellation_rate DESC;


-- ----------------------------------------------------------------------------
-- 10. TOP COUNTRIES BY BOOKINGS
-- ----------------------------------------------------------------------------
WITH country_analysis AS (
    SELECT 
        country,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate,
        ROUND(AVG(adr), 2) AS avg_daily_rate
    FROM hotel_bookings
    WHERE country IS NOT NULL
    GROUP BY country
)
SELECT * FROM country_analysis
ORDER BY total_bookings DESC
LIMIT 10;
