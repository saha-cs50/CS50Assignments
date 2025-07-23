-- Keep a log of any SQL queries you execute as you solve the mystery.


--to find any crimes that occured at the same place and time as the report of the theft of duck
SELECT id, description FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';
--crime took place at 10:15, found in interview 295 there were 3 witnesses who were interviewed the same day and mentioned the bakery

--finding the interviews and names of people wo were interviewed based on the day of interviewing and the mention of bakery
SELECT id, name, transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%';
--Ruth (161) says that 10 minutes (10:25) after theft thief got into car in baking parking lot check cars on cams that left baking parking lot at time
--Eugene (162) saw thief withdrawing money at ATM on Leggett Street earlier that day
--Raymond (163) saw thief talking to someone on phone as they left bakery, thief planned to take earliest flight out on july 29th 2021, asked person on call to purchase ticket


--checking bakery security footage at 10:25 that day
SELECT activity, license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 and minute BETWEEN 15 AND 25;
--eight cars left bakery at the time with license plates G412CB7, L93JTIZ, 322W7JE, 0NTHK55

--finding people with those license plates
SELECT name FROM people WHERE license_plate IN(SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 and minute BETWEEN 15 AND 25);
--Iman, Sofia, Diana, Kelsey

--finding people who withdrew from ATM earlier that day
SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN(SELECT account_number FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location ='Leggett Street' AND transaction_type = 'withdraw' ));

--phone call
SELECT caller, receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60);
--finding people based on license with that phone number
--narrowing down options from all previous findings, can either be diana or bruce


--finding destination city
SELECT destination_airport_id,hour,minute FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id IN (SELECT id FROM airports WHERE city = 'Fiftyville') ORDER BY hour;
SELECT city FROM airports WHERE id = 4;
--ESCAPING TO NEW YORK CITY

--finding flight taken
SELECT city,id FROM airports;
SELECT id FROM flights WHERE origin_airport_id = 8 AND destination_airport_id = 4 AND year = 2021 AND month = 7 AND day = 29 AND hour = 8 AND minute = 20;
--flight 36 taken

--checking to see if diana or bruce is passenger on flight 36
SELECT name FROM people WHERE passport_number IN(SELECT passport_number FROM passengers WHERE flight_id = 36);
--bruce is in flight
--bruce is thief

--finding accomplice BRUCE called
SELECT name,phone_number FROM people WHERE name = 'Bruce';
SELECT caller, receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;
SELECT name FROM people WHERE phone_number = '(375) 555-8161';
--ROBIN

