$(function(){
	$('#Q-type li').click(function(){
              $('#Q-type li').removeClass('active');
              $(this).addClass('active');

            });

});
 $(function(){

 	$('#btn').click(function(){
 		var textarea=$('textarea').val();
		$("#comment").append("<p>"+textarea+"</p>");
		
	});
 });  
 // $(function(){

 // 	$('#Toggle').click(function(){

 // 		$('section').slideToggle(1000);

	// // $('.main-sidebar').animate(width:'0px','slow');

 // 	})
 // }) 
   

// jQuery(document).ready(function($) { 
//     var isLateralNavAnimating = false; 
//     //o打开或关闭导航菜单 
//     $('#Toggle').on('click', function(event) { 
//         event.preventDefault(); 
//         //若动画正在进行，则停止  
//         if (!isLateralNavAnimating) { 
//             if ($(this).parents('.csstransitions').length > 0) 
//                 isLateralNavAnimating = true; 
 
//             $('aside').toggleClass('none-sidebar'); 
//             $('.cd-navigation-wrapper').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function() { 
//                 //动画结束 
//                 isLateralNavAnimating = false; 
//             }); 
//         } 
//     }); 
// });
  
 $(function(){
 	$('#ask-btn').click(function(){
        // $('.addQuestion').attr('style','display:block');
         $('.addQuestion').slideToggle(400);
 	});
 });
 $(function(){
 	$('#ask-close').click(function(){
        // $('.addQuestion').attr('style','display:block');
         $('.addQuestion').slideUp(400);
 	});
 });