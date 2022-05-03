function getPositionY( element ) {
    var rect = element.getBoundingClientRect();
    return rect.top
    
}

const coloringImage = function(){
    var windowWidth = window.innerWidth;
    var windowHeight = window.innerHeight;

    var images = $("img");

    let y = getPositionY(images[2]);

    console.log(y);
    if(windowWidth<550 && windowHeight<700){
        images.each(function(index){
            let y = getPositionY(images[index]);
            if(-100<y && y<300){
                $(this).addClass("colored");  
            }else{
                $(this).removeClass("colored");  
            }   
        })        
    }
}
window.addEventListener("scroll", coloringImage);

document.addEventListener("DOMContentLoaded", coloringImage);


$("#images").change(function() {
    var els = "";

    for(let i = 0; i<this.files.length; i++){
        els += "<p class='text-primary'>"+this.files[i].name+"</p>";
        console.log(this.files[i].name)
    }
    $("#file-container").html(" ")
    $("#file-container").append(els);

    
});