// Atlas-authored reference: resolve only after the entire transaction commits.
export function writeRecords(db, store, records) {
  return new Promise((resolve, reject) => {
    let tx;
    try {
      tx = db.transaction(store, 'readwrite');
      tx.oncomplete = () => resolve();
      tx.onabort = tx.onerror = () => reject(new Error('storage_write'));
      for (const record of records) tx.objectStore(store).put(record);
    } catch (error) {
      try { tx?.abort(); } catch {}
      reject(error);
    }
  });
}
