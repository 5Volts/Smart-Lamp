function send_color(val){
  rgb = hex2rgb(val);
  console.log(rgb);
  var r = rgb['r'];
  var g = rgb['g'];
  var b = rgb['b'];

  $.ajax({
    url:'/smart_lamp_color?r='+r+'&g='+g+'&b='+b,
    dataType:'json',
    success:function(data){
      console.log(data);
    }
  })

}

function send_brightness(val){

  $.ajax({
    url:'/smart_lamp_brightness?brightness=' + val,
    success:function(data){
      console.log(data);
    }
  })
  
}

function hex2rgb(hex){
  var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? {
    r: parseInt(result[1], 16),
    g: parseInt(result[2], 16),
    b: parseInt(result[3], 16)
  } : null;
}
