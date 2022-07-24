let prevVal = '';
document.getElementById('exprezzion').addEventListener('input', function(e){
	if (this.checkValidity()) {
		prevVal = this.value;
	} else {
		this.value = prevVal;
	}
});

function calc() {
	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'calc', true);
	xhr.setRequestHeader('Content-Type', 'text/plain');
	xhr.onreadystatechange = function () {
		if (xhr.readyState === 4 && xhr.status === 200) {
			document.getElementById('res').value = xhr.responseText;
		}
	};
	xhr.send(document.getElementById('exprezzion').value);
}
