CREATE TABLE body_performance (
  age FLOAT,
  gender varchar(1),
  height FLOAT,
  weight FLOAT,
  body_fat FLOAT,
  diastolic FLOAT,
  systolic FLOAT,
  bend_forward FLOAT,
  grip_force FLOAT,
  sit_ups FLOAT,
  broad_jump FLOAT,
  class varchar(1),

  PRIMARY KEY (age, gender, height, weight, body_fat, diastolic, systolic, bend_forward, grip_force, sit_ups, broad_jump)
);

CREATE TEMPORARY TABLE csv_table (
  age float,
  gender varchar(1),
  height float,
  weight float,
  body_fat float,
  diastolic float,
  systolic float,
  bend_forward float,
  grip_force float,
  sit_ups float,
  broad_jump float,
  class varchar(1)
);

COPY csv_table FROM '/tmp/bodyPerformance.csv' WITH (FORMAT csv, HEADER true);

DO $$
DECLARE
  row csv_table%ROWTYPE;
BEGIN
  FOR row IN (SELECT * FROM csv_table)
  LOOP
    BEGIN
      INSERT INTO body_performance (age, gender, height, weight, body_fat, diastolic, systolic, bend_forward, grip_force, sit_ups, broad_jump, class)
      VALUES (row.age, row.gender, row.height, row.weight, row.body_fat, row.diastolic, row.systolic, row.bend_forward, row.grip_force, row.sit_ups, row.broad_jump, row.class)
      ON CONFLICT DO NOTHING;
    END;
  END LOOP;
END $$;