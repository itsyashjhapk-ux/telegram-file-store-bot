export default function handler(req, res) {

  const { id } = req.query;

  if (!id) {
    res.status(400).send("Invalid Link");
    return;
  }

  const telegramLink = `https://t.me/share/url?url=${id}`;

  res.writeHead(302, {
    Location: telegramLink
  });

  res.end();
}
