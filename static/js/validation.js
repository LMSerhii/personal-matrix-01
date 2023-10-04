function validateForm()
{
let x=document.forms["order-service"]["user-name"].value;
if (x==null || x=="")
  {
  alert("Необходимо заполнить поле Имя!");
  return false;
  }
}