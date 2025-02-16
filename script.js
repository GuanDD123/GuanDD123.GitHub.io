window.onload = function () {
    const savedWallpaper = localStorage.getItem("backgroundImage");
    if (savedWallpaper) {
        document.body.style.backgroundImage = `url(${savedWallpaper})`;
    } else {
        document.body.style.backgroundImage = "url('wallpaper/bc13haet9350hio.png')";
    }
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

        const wallpaper = { id: 1, imageData: dataUrl }; // 1是图片的唯一标识符
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
            storeImageInIndexedDB(e.target.result);
            document.body.style.backgroundImage = `url(${e.target.result})`;
        };
        reader.readAsDataURL(file);
    }
}

/*
function changeWallpaper(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            document.body.style.backgroundImage = `url(${e.target.result})`;
            localStorage.setItem("backgroundImage", e.target.result);
        };
        reader.readAsDataURL(file);
    }
}
*/
