const bouquet = document.querySelector("#bouquet");

document.querySelectorAll(".flower-picker button").forEach(button => {
  button.addEventListener("click", () => {
    createFlower(button.dataset.flower);
  });
});

function createFlower(type) {
  const flower = document.createElement("div");

  flower.className = "flower";
  flower.textContent = getFlowerEmoji(type);

  flower.style.left = "50%";
  flower.style.top = "50%";

  bouquet.appendChild(flower);

  makeDraggable(flower);
}

function getFlowerEmoji(type) {
  const flowers = {
    rose: "🌹",
    tulip: "🌷",
    sunflower: "🌻",
    daisy: "🌼",
    cherry: "🌸"
  };

  return flowers[type];
}

function makeDraggable(element) {
  let dragging = false;

  element.addEventListener("pointerdown", e => {
    dragging = true;
    element.setPointerCapture(e.pointerId);
  });

  element.addEventListener("pointermove", e => {
    if (!dragging) return;

    const rect = bouquet.getBoundingClientRect();

    element.style.left =
      `${e.clientX - rect.left}px`;

    element.style.top =
      `${e.clientY - rect.top}px`;
  });

  element.addEventListener("pointerup", () => {
    dragging = false;
  });
}