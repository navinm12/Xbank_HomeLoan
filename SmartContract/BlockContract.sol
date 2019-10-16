pragma solidity 0.4.25;

contract Xbank {
  struct detail{
      string name ;
      uint salary;
      uint documentid;
      uint estimation;
      bool dveri;
      bool vsal;
  }
 
  struct Banklegal_Advisor{
      uint docid;
     
  }
 
  struct BankAuthorized_Civil{
      uint civil_estimation;
      uint vesti;
  }
 
 
 

  mapping (address => detail) message;
  mapping (address=> Banklegal_Advisor) advisor;
  mapping (address=> BankAuthorized_Civil) civil_Advisor;
 

  function Customer(address _recipient, string _message,uint _salary,uint _documentid,uint _estimation)public{
    message[_recipient].name = _message;
    message[_recipient].salary = _salary;
    message[_recipient].documentid=_documentid;
    message[_recipient].estimation=_estimation;
  }
 
 
    function Bankacess() view public returns (string , uint, bool,bool){
   
    return(message[msg.sender].name,message[msg.sender].salary,message[msg.sender].dveri,message[msg.sender].vsal);
  }
 
  function BankAdvisor(address _recipient)  public{
     advisor[_recipient].docid=message[msg.sender].documentid;
  }
 
 
   function bankadvisoraccess() view public returns (uint){
    return(advisor[msg.sender].docid);
  }
 
 
  function Civil_advisor (address _recipient)  public{
     civil_Advisor[_recipient].civil_estimation=message[msg.sender].estimation;
  }
 
 
   function civiladvisoraccess() view public returns (uint){
    return(civil_Advisor[msg.sender].civil_estimation);
  }
 

    function documentver(address _bankaddress) public {
           
            if(advisor[msg.sender].docid==123456789)
            {
                message[_bankaddress].dveri=true;
               
            }
           
            else
            {
                message[_bankaddress].dveri=false;
               
            }
    }
    function mest(address _bankforestimation) public{
       
       
         if(civil_Advisor[msg.sender].civil_estimation>100000 && civil_Advisor[msg.sender].civil_estimation<500000 )
         {
       
            message[_bankforestimation].vsal=true;
          }
         
         
          else
          {
              message[_bankforestimation].vsal=false;
          }
       
    }
   
   
   
       
}
