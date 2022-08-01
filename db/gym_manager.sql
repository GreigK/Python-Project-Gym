DROP TABLE bookings;
DROP TABLE members;
DROP TABLE activitys;
DROP TABLE activity_types;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    premium BOOLEAN
);

CREATE TABLE activity_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE activitys (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    activity_type_id INT REFERENCES activity_types(id) ON DELETE CASCADE
);


CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    activity_id SERIAL NOT NULL REFERENCES activitys(id) ON DELETE CASCADE,
    member_id SERIAL NOT NULL REFERENCES members(id) ON DELETE CASCADE
);

