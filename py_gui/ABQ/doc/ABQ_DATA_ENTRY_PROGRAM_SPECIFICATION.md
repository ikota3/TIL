# ABQ Data Entry Program Specification

## Description

The program is being created to minimize data entry errors for laboratory measurements.

## Functionality

### Required

- allow all relevant, valid data to be entered, as per the field chart

- append entered data to CSV file

  - The CSV file must have a filename
    of abq_data_record_CURRENT_DATE.csv,
    where CURRENT_DATE is the date of the
    checks in ISO format(YYYY-MM-DD)

  - The CSV file must have all the fields as per the chart

- enforce correct data types per field

The program should try, whenever possible, to:

- enforce reasonable limits on data entered
- Auto-fill data
- Suggest likely correct values
- Provide a smooth and efficient workflow

### Not Required

- Allow editing of data. This can be done in LibreOffice if necessary

- Allow deletion of data

## Limitations

- Be efficiently operable by keyboard-only users
- Be accessible to color blind users
- Run on Debian Linux
- Run acceptably on low-end PC

## Data dictionary

| Field         | Datatype | Units | Range         | Descripton           |
| ------------- | -------- | ----- | ------------- | -------------------- |
| Date          | Date     |       |               | Date of record       |
| Time          | Time     |       | 8, 12, 16, 20 | Time period          |
| Lab           | String   |       | A - E         | Lab ID               |
| Technician    | String   |       |               | Technician name      |
| Plot          | Int      |       | 1 - 20        | Plot ID              |
| Seed sample   | String   |       |               | Seed sample ID       |
| Fault         | Bool     |       |               | Fault on sensor      |
| Light         | Decimal  | klx   | 0 - 100       | Light at plot        |
| Humidity      | Decimal  | g/m³  | 0.5 - 52.0    | Abs humidity at plot |
| Temperature   | Decimal  | °C    | 4 - 40        | Temperature at plot  |
| Blossoms      | Int      |       | 0 - 1000      | # blossoms in plot   |
| Fruit         | Int      |       | 0 - 1000      | # fruits in plot     |
| Plants        | Int      |       | 0 - 20        | # plants in plot     |
| Max height    | Decimal  | cm    | 0 - 1000      | Ht of tallest plant  |
| Min height    | Decimal  | cm    | 0 - 1000      | Ht of shortest plant |
| Median height | Decimal  | cm    | 0 - 1000      | Median ht of plants  |
| Notes         | String   |       |               | Miscellaneous notes  |
