async function load(){
  const ul = document.getElementById("list");
  ul.innerHTML = "Carregando...";
  try {
    const res = await fetch("http://localhost:8000/softwares");
    if (!res.ok) throw new Error("HTTP " + res.status);
    const softwares = await res.json();
    ul.innerHTML = "";
    softwares.forEach(s => {
      const li = document.createElement("li");
      li.textContent = `${s.id}: ${s.name}`;
      ul.appendChild(li);
    });
  } catch (e) {
    ul.innerHTML = "Erro: " + e.message;
  }
}
