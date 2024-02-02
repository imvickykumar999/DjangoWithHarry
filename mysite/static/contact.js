
function submitLoginForm(event){
    event.preventDefault();
    let flname = event.target['name'].value;
    let email = event.target['email'].value;
    let phone = event.target['phone'].value;
    let desc = event.target['desc'].value;
    let text = ` <name> ` + flname + ` <email> ` + email + ` <phone> ` + phone + ` <desc> ` + desc;
    
    let ID = 5721393154;
    let API = '6556542346:AAFPNkrk6FLdIne_-pe_5M-DSMy4szyLRjw';
    let url = `https://api.telegram.org/bot${API}/sendMessage?chat_id=${ID}&text=${text}`;
    fetch(url);
    event.target.reset();
}
