function validateForm()
{
let x=document.forms["order-service"]["user-name"].value;
if (x==null || x=="")
  {
  alert("Необходимо заполнить поле Имя!");
  return false;
  }
let y=document.forms["order-service"]["user-day"].value;
if (y==null || y=="")
  {
  alert("Необходимо заполнить поле День Рождения!");
  return false;
  } else if (y < 1 || y > 31) {
  alert("Не коректно введен День Рождения!");
  return false;
  }

let v=document.forms["order-service"]["user-month"].value;
if (v==null || v=="")
  {
  alert("Необходимо заполнить поле Месяц Рождения!");
  return false;
  } else if (v < 1 || v > 12) {
  alert("Не коректно введен Месяц Рождения!");
  return false;
  }


let b=document.forms["order-service"]["user-year"].value;
if (b==null || b=="")
  {
  alert("Необходимо заполнить поле Год Рождения!");
  return false;
  } else if (b < 1) {
  alert("Не коректно введен Год Рождения!");
  return false;
  }
}