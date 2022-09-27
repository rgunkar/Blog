# SOLID Principles explained via examples of the Codes written in this Repo

Run the following commands
Create virtualenv(Python 3.9) and install all the requirements
<code> $ pip install -r requirements.txt </code>
# Run the flask app
<code> $ python runserver.py </code>

Behind all the examples a SOLID Principle has been used. 
Please download the PDF for the same.

You will see the following screen upon running this app.

![Screenshot 2022-09-27 at 11 30 40 AM](https://user-images.githubusercontent.com/68590761/192445138-823d323d-1433-41df-852e-237739014315.png)

Functionality of the top 3 functions is simple and has 1 SOLID Principle in the backgroud each and for rest 2 I have kept real examples. Let's see them one by one.

# Dependency Inversion
![Screenshot 2022-09-27 at 11 32 21 AM](https://user-images.githubusercontent.com/68590761/192445388-51921539-f31a-4b48-b93e-d5708410ca02.png)

Click on the above link to see how Code in **Admin-api-2** repo is breaking the Dependency Inversion Principle and how it can be corrected.

# Liskov Substitution Principle
![Screenshot 2022-09-27 at 11 34 03 AM](https://user-images.githubusercontent.com/68590761/192445661-e2f35196-50f7-4a6a-8721-78ede2218ad0.png)

Click on each link to see how Code in **admin-api-1** is violating LSP Principle & how we can correct it.

# Single Responsibility Principle
![Screenshot 2022-09-27 at 11 38 36 AM](https://user-images.githubusercontent.com/68590761/192446268-de740ca2-fbd3-4676-bb62-2b61c5f6d4b0.png)

Clicking on the above link gives us a text response.
Let's see how SRP is being used in backgroud.

![Sc![Uploading Screenshot 2022-09-27 at 11.48.08 AM.png…]()
reenshot 2022-09-27 at 11 45 24 AM](https://user-images.githubusercontent.com/68590761/192447361-2e103002-a0b2-4f6d-a575-5652df9b90a4.png)

As we can see, Hero Class has only one responsibility, ReturnHeroSpec also has one responsibily and we have different class for various features like HasHealth, CanAttack and any new class will need to just inherit the base Hero Class and no other class will be modified.
We have only one reason to change the ReturunHeroSpec..that is when any more spec is to be returned.

# Open Closed Principle
![Screenshot 2022-09-27 at 11 56 11 AM](https://user-images.githubusercontent.com/68590761/192449152-c5eb5440-fa30-4e07-82d1-6fa2353cd819.png)

As we can see, BlockAddress is open for extension and is extended by FullAddress and is closed for modification and has no need of further change.

2nd link to print superman's address is using the above code in backgroud.

![Screenshot 2022-09-27 at 11 57 55 AM](https://user-images.githubusercontent.com/68590761/192449460-38b61821-8590-4b0f-9952-e04a320e744a.png)



