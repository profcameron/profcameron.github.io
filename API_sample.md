# Sample API Documentation
This is a sample API documentation for a fictional workout builder application. Note that all of these requests will return a 404 error for the moment.

## Postman Collection
You can [import this Postman collection](./workout_API_Postman.json) of the Workout Builder requests. If you have never imported a collection before, view the [Postman Import an API documentation](https://learning.postman.com/docs/designing-and-developing-your-api/importing-an-api/) for assistance (it's short; 5 steps).

## Base URL
The following is the base URL for this exercise:
http://www.example.com/api/v1

## Retrieve All Exercises
Returns a list of all exercises available in the workout builder.

### Endpoint
`GET /exercises`

### Request Example
`curl -X GET 'http://www.example.com/api/v1/exercises'`

### Response Example
```
[
   {
       "id": 101,
       "author": "Milagros Hernandez",
       "title": "Bicep Curl",
       "level": "basic",
       "muscle": "bicep",
       "instructions": "Stand with your feet apart, approximately shoulder-width apart, with a dumbbell in each hand. With your palms facing upwards and your elbows close to the body, curl the weights up. Pause at the top and slowly lower the dumbbells."
   },
   {
       "id": 102,
       "author": "Corey Miller",
       "title": "Shoulder Shrug",
       "level": "intermediate",
       "muscle": "trapezius",
       "instructions": "Stand with your feet apart, approximately shoulder-width apart, with your arms hanging at your sides. Lift your shoulders towards your ears, holding the position at the peak for a moment. Slowly lower your shoulders to your starting position."
   },
]
```

## Retrieve a Specific Exercise
Returns an exercise, based on the id number.

### Endpoint
`GET /exercises/{id}`

### Parameter Information
Parameters | Data Type | Description
-|-|-|
id | int | The unique id number of a specific exercise.


### Request Example
`curl -X GET 'http://www.example.com/api/v1/exercises/101'`

### Response Example
```
{
    "id": 101,
    "author": "Milagros Hernandez",
    "title": "Bicep Curl",
    "level": "basic",
    "muscle": "bicep",
    "instructions": "Stand with your feet apart, approximately shoulder-width apart, with a dumbbell in each hand. With your palms facing upwards and your elbows close to the body, curl the weights up. Pause at the top and slowly lower the dumbbells."
}
```

## Retrieve Exercises for a Muscle
Returns a filtered list of exercise, based on the muscle specified.

### Endpoint
`GET /exercises?muscle=value`

### Parameter Information
Parameters | Data Type | Description
-|-|-|
value | String | The body part for which you want to search for. Case insensitive.


### Request Example
`curl -X GET 'http://www.example.com/api/v1/exercises?muscle=bicep'`

### Response Example
```
[
    {
        "id": 101,
        "author": "Milagros Hernandez",
        "title": "Bicep Curl",
        "level": "basic",
        "muscle": "bicep",
        "instructions": "Stand with your feet apart, approximately shoulder-width apart, with a dumbbell in each hand. With your palms facing upwards and your elbows close to the body, curl the weights up. Pause at the top and slowly lower the dumbbells."
    },
    {
       "id": 103,
       "author": "Anjana Sharma",
       "title": "Inclined Bicep Curl",
       "level": "advanced",
       "muscle": "bicep",
       "instructions": "Adjust a bench at a 45 degree angle. With your palms up, resting on the bench, curl the weights. Pause at the top and slowly lower the dumbbells."
   },
]
```
