import numpy as np
from sklearn.linear_model import LinearRegression

car_brands = np.array(['Toyota', 'Mazda', 'Mitsubishi', 'Honda'])
ages = np.array([5, 7, 15, 28])
mileages = np.array([30530, 90000, 159899, 270564])
ages_2d = ages.reshape(-1, 1)
model = LinearRegression()
model.fit(ages_2d, mileages)

def predict_mileage(car_brand, age):
    brand_index = np.where(car_brands == car_brand)[0][0]
    age_2d = np.array([[age]])
    predicted_mileage = model.predict(age_2d)
    return predicted_mileage[0]

new_car_brand = 'Toyota'
new_car_age = 5  
predicted_mileage = predict_mileage(new_car_brand, new_car_age)
print(f"Predicted mileage for a {new_car_brand} car with {new_car_age} years of age: {predicted_mileage:.2f} km")
