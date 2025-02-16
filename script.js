window.onload = function () {
    const request = indexedDB.open('wallpaperDB', 1);
    request.onsuccess = function (event) {
        const db = event.target.result;
        const transaction = db.transaction(['wallpapers'], 'readonly');
        const objectStore = transaction.objectStore('wallpapers');

        const getRequest = objectStore.get(1);
        getRequest.onsuccess = function () {
            const wallpaper = getRequest.result;
            if (wallpaper && wallpaper.imageData) {
                document.body.style.backgroundImage = `url(${wallpaper.imageData})`;
            } else {
                document.body.style.backgroundImage = "url('wallpaper/bc13haet9350hio.png')";
            }
        };
        getRequest.onerror = function () {
            document.body.style.backgroundImage = "url('wallpaper/bc13haet9350hio.png')";
        };
    };

    request.onerror = function (event) {
        console.error('打开 IndexedDB 失败:', event.target.error);
        document.body.style.backgroundImage = "url('wallpaper/bc13haet9350hio.png')";
    };
};

function storeImageInIndexedDB(dataUrl) {
    const request = indexedDB.open('wallpaperDB', 1);
    request.onupgradeneeded = function (event) {
        const db = event.target.result;
        const objectStore = db.createObjectStore('wallpapers', { keyPath: 'id' });
        objectStore.createIndex('by_image', 'imageData', { unique: false });
    };

    request.onsuccess = function (event) {
        const db = event.target.result;
        const transaction = db.transaction(['wallpapers'], 'readwrite');
        const objectStore = transaction.objectStore('wallpapers');

        const wallpaper = { id: 1, imageData: dataUrl };
        const addRequest = objectStore.add(wallpaper);
        addRequest.onsuccess = function () {
            console.log('图片已成功存储到 IndexedDB');
        };
        addRequest.onerror = function (event) {
            console.error('存储到 IndexedDB 失败:', event.target.error);
        };
    };

    request.onerror = function (event) {
        console.error('IndexedDB 打开失败:', event.target.error);
    };
}

function changeWallpaper(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const result = e.target.result;
            if (result) {
                storeImageInIndexedDB(result);
                document.body.style.backgroundImage = `url(${result})`;
            } else {
                console.error("加载图片失败，result 为空");
            }
        };
        reader.readAsDataURL(file);
    }
}
