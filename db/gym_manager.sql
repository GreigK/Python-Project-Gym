DROP TABLE bookings;
DROP TABLE members;
DROP TABLE activitys;
DROP TABLE activity_types;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE activity_type (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE activitys (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    name VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    activity_id INT REFERENCES activity(id),
    review TEXT
);

