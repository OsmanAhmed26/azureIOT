SELECT 
    temperature, 
    humidity, 
    System.Timestamp AS timestamp 
INTO 
    [YourOutputAlias] 
FROM 
    [YourInputAlias]
