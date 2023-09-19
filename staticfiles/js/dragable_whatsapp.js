
        const draggableElement = document.getElementById('draggableElement');

        let offsetX, offsetY, isDragging = false;

        function startDragging(e) {
            isDragging = true;
            if (e.type === 'touchstart') {
                offsetX = e.touches[0].clientX - draggableElement.getBoundingClientRect().left;
                offsetY = e.touches[0].clientY - draggableElement.getBoundingClientRect().top;
            } else {
                offsetX = e.clientX - draggableElement.getBoundingClientRect().left;
                offsetY = e.clientY - draggableElement.getBoundingClientRect().top;
            }
            draggableElement.style.cursor = 'grabbing';
        }

        function moveElement(e) {
            if (!isDragging) return;
            e.preventDefault();
            
            let x, y;

            if (e.type === 'touchmove') {
                x = e.touches[0].clientX - offsetX;
                y = e.touches[0].clientY - offsetY;
            } else {
                x = e.clientX - offsetX;
                y = e.clientY - offsetY;
            }

            // Ensure the element stays within the viewport boundaries.
            x = Math.max(0, Math.min(window.innerWidth - draggableElement.offsetWidth, x));
            y = Math.max(0, Math.min(window.innerHeight - draggableElement.offsetHeight, y));

            draggableElement.style.left = `${x}px`;
            draggableElement.style.top = `${y}px`;
        }

        function stopDragging() {
            isDragging = false;
            draggableElement.style.cursor = 'grab';
        }

        draggableElement.addEventListener('mousedown', startDragging);
        draggableElement.addEventListener('touchstart', startDragging);

        document.addEventListener('mousemove', moveElement);
        document.addEventListener('touchmove', moveElement);

        document.addEventListener('mouseup', stopDragging);
        document.addEventListener('touchend', stopDragging);

        draggableElement.addEventListener('dragstart', (e) => {
            e.preventDefault();
        });


