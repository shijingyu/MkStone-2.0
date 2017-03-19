// window scroll
var windowScroll=function(){
$(window).scroll(function(){

	var scrollPos=$(this).scrollTop();
	
	if($(window).scrollTop()>70){
		$('nav').addClass('navbar-default');
	}
	else{
		$('nav').removeClass('navbar-default');
	}

});


// Superfish Sub Menu Click ( Mobiles/Tablets )


}
	var mobileClickSubMenus = function() {

		$('body').on('click', '.fh5co-sub-ddown', function(event) {
			event.preventDefault();
			var $this = $(this),
				li = $this.closest('li');
			li.find('> .fh5co-sub-menu').slideToggle(200);
		});

	};
$(function(){

	windowScroll();
	mobileClickSubMenus();
});
$('.carousel').carousel({
  interval: 3000
})
