// 素材列表：GET 返回 [{key, name, category}]
const { getStore } = require('@netlify/blobs');

exports.handler = async () => {
  try {
    const store = getStore('kk-stickers');
    const items = [];
    const { blobs } = await store.list({ prefix: 'stickers/' });
    for (const entry of blobs) {
      const parts = entry.key.split('/'); // stickers/{category}/{ts}_{name}
      const name = (parts[parts.length - 1] || '').replace(/^\d+_/, '');
      let title = '';
      try {
        const meta = await store.getMetadata(entry.key);
        title = (meta && meta.title) || '';
      } catch (e) { /* ignore */ }
      items.push({
        key: entry.key,
        name,
        title,
        category: parts[1] || '其他',
      });
    }
    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
      body: JSON.stringify(items),
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: String((err && err.message) || err) }),
    };
  }
};
