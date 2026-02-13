var choice=prompt("welcome to area calculator.\n Please enter your choice(1-4) \n 1. Area of rectangle \n 2. Area of triangle \n 3. Area of Circle \n 4. Area of Parellogram")

if (choice=='1')
   {
    var l=prompt('Enter the length: ');
    var w=prompt('Enter the width: ');
    var area=Number(w)*Number(l);
    alert('the area is : '+area);
   }

if (choice=='3')
   {
    var r =prompt('Enter the radius: ');
    var area =3.14*Number(r)*Number(r);
    alert('The area is'+area);
    circumference=2*3.1416*Number(r)
    alert('the Circle circumference is: '+circumference)
   }

if (choice=='2')
   {
    var h =prompt('Enter the height: ');
    var b =prompt('Enter the base: ');
    var area =0.5*Number(h)*Number(b);
    alert('The area is'+area);
    var c =prompt('Enter the value of c: ')
    var perimeter =Number(h)+Number(a)+Number(c);
    alert('The Triangle perimeter is'+perimeter);
    
   }

if (choice=='4')
   {
    var h =prompt('Enter the height: ');
    var cb =prompt('Enter the corresponding base: ');
    var a =prompt('Enter the other side of base')
    var area =Number(h)*Number(cb);
    alert('The area is'+area);
   }

