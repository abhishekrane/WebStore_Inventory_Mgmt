
// Abhishek Rane
// REd id- 822056658
// Account- Jadrn034 




$(document).ready(function(){

window.addEventListener( "pageshow", function ( event ) {
      var historyTraversal = event.persisted || ( typeof window.performance != "undefined" && window.performance.navigation.type === 2 );
      if ( historyTraversal ) {
      window.location.href = "http://jadran.sdsu.edu/~jadrn034/proj1/index.html";
      }


});



});
$('#sku').blur( function(){
             if($("#sku").val() == "")
             {
                
             }
         else{
            var Data = $('#sku').serialize();
            $.ajax({
                    url: "/perl/jadrn034/check_dup.cgi",
                    type: "get",
                    data: Data,
                    success: function(response){
                        if(response == "OK"){
                            $("#addmessage").css("display","block");
                            $("#addmessage").html("The sku is Unique");
                            $("#addmessage").fadeOut(1000);
                           
                    } else if(response == "DUPLICATE"){
                           
                           alert(response);
                            $("#sku").val("");
                         
                        }
                    }
            });
        }
         });






              
        

$('#delete').click( function(e){
        e.preventDefault();
             
            
           var Data = $('#deleteForm').serialize();
            $.ajax({
           
                    url: "http://jadran.sdsu.edu/perl/jadrn034/deleteItem.cgi",
                    type: "post",
                    data: Data,
                    
                    success: function(response){
                         
                        
                        alert(response);
                    
                         
                         $("#sku_del").val("");
                         $("#category_del").val("");
                         $("#vendor_del").val("");
                          $("#mfid_del").val("");
                           $("#desc_del").val(""); 
                           $("#features_del").val("");
                            $("#cost_del").val("");
                             $("#retail_del").val("");
                            $("#quantity_del").val("");
                            $("#pic_del").attr('src', '');

                    
                    }
            });
              
         });


$('#reset_add').click( function(){
      
       
       $("#pic_add").attr('src', '');
       
              
         });

$('#reset_upd').click( function(){
      
      $('#sku_upd').prop('disabled',false);
       $("#pic_upd").attr('src', '');
       
              
         });

$('#reset_del').click( function(){
      
       
       $("#pic_del").attr('src', '');
       
              
         });










$('#sku_upd').blur( function(){
            
            
            var Data = $('#sku_upd').serialize();
            $.ajax({
                    url: "/perl/jadrn034/update.cgi",
                    type: "get",
                    data: Data,
                    success: function(response){
                        if(response == "No such SkU"){
                           alert(response);
                           $("#sku_upd").val("");

                           
                    } else {
                           
                          
                          var arrayData = explodeArray(response,'|');
                           
                           $("#sku_upd").val(arrayData[0]);

                            $("#category_upd").val(arrayData[1]);
                            $("#vendor_upd").val(arrayData[2]);
                          $("#mfid_upd").val(arrayData[3]);
                           $("#desc_upd").val(arrayData[4]); 
                           $("#features_upd").val(arrayData[5]);
                            $("#cost_upd").val(arrayData[6]);
                             $("#retail_upd").val(arrayData[7]);
                            $("#quantity_upd").val(arrayData[8]);
                           
                            var img= "http://jadran.sdsu.edu/~jadrn034/proj1/file_upload/"+arrayData[9];
                             
                            $("#pic_upd").attr('src',img);
                            $("#pic_upd2").val(arrayData[9]);
                            $("#pic_upd3").val(arrayData[9]);
                            

                                }
 
                        
                    }
            });
        
         });


$('#sku_del').blur( function(){
             if($("#sku_del").val() == "")
             {
                
             }
             else{
            var del = $('#sku_del').serialize();
            $.ajax({
                    url: "/perl/jadrn034/delete.cgi",
                    type: "get",
                    data: del,
                    success: function(response){
                        if(response == "No such SkU"){
                           alert(response);
                           $("#sku_del").val("");
                           
                    } else {

                          var array = explodeArray(response,'|');
                            
                            $("#category_del").val(array[1]);
                            $("#vendor_del").val(array[2]);
                          $("#mfid_del").val(array[3]);
                           $("#desc_del").val(array[4]); 
                           $("#features_del").val(array[5]);
                            $("#cost_del").val(array[6]);
                             $("#retail_del").val(array[7]);
                            $("#quantity_del").val(array[8]);

                        var img= "http://jadran.sdsu.edu/~jadrn034/proj1/file_upload/"+array[9];
                            
                            $("#pic_del").attr('src',img);


                                }
 
                        
                    }
            });
        }
         });


function explodeArray(item,delimiter) {
tempArray=new Array(1);
var Count=0;
var tempString=new String(item);

while (tempString.indexOf(delimiter)>0) {
tempArray[Count]=tempString.substr(0,tempString.indexOf(delimiter));
tempString=tempString.substr(tempString.indexOf(delimiter)+1,tempString.length-tempString.indexOf(delimiter)+1);
Count=Count+1
}

tempArray[Count]=tempString;
return tempArray;
}


