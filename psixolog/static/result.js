window.onload = function(){
    document.getElementById("cmd")
    .addEventListener("click",()=>{
    const page = this.document.getElementById("result-box");
    var opt = {
          margin:       1,
          filename:     'myfile.pdf',
          image:        { type: 'jpeg', quality: 0.98 },
          html2canvas:  { scale: 2 },
          jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
    };
    html2pdf().from(page).set(opt).save();
    })



}