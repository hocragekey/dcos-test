from __future__ import print_function

import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("AggregateByCountryAndYear")\
        .getOrCreate()

    #TODO: Read CSV to data frame
    #TODO: /raw/GlobalLandTemperaturesByCity.csv
    #TODO: File Format:
    #TODO: dt,AverageTemperature,AverageTemperatureUncertainty,City,Country,Latitude,Longitude
    #TODO: Write raw DF to HDFS as city
    #TODO: Sum up data by Country and write DF to HDFS as country

    lines = spark.textFile("hdfs://hdfs/raw/GlobalLandTemperaturesByCity.csv")
    parts = lines.map(lambda l: l.split(","))
    cityTemp = parts.map(lambda p: (p[0], p[1], p[2], p[3], p[4], p[5], p[6]))

    s = "dt,AverageTemperature,AverageTemperatureUncertainty,City,Country,Latitude,Longitude
    fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split(",")]
    schema = StructType(fields)

    df = spark.createDataFrame(cityTemp, schema);
    count = df.count()

    print "data frame count %d" count
    #TODO: Write out partitioned DataFrame

    spark.stop()
