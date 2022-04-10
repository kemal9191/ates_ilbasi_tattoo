function getPositionY( element ) {
    var rect = element.getBoundingClientRect();
    return rect.top
    
}

window.addEventListener("scroll", function(){
    var windowWidth = window.innerWidth;
    var windowHeight = window.innerHeight;

    var images = $("img");

    let y = getPositionY(images[2]);

    console.log(y);
    if(windowWidth<500 && windowHeight<600){
        images.each(function(index){
            let y = getPositionY(images[index]);
            if(-100<y && y<300){
                $(this).addClass("colored");  
            }else{
                $(this).removeClass("colored");  
            }   
        })        
    }
})
