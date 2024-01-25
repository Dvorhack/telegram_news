use teloxide::prelude::*;
use std::env;

#[tokio::main]
pub async fn telegram_thread(rx: std::sync::mpsc::Receiver<String>) {
    println!("Hello from Telegram Thread!");

    let token = env::var("TELEGRAM_TOKEN").expect("$TELEGRAM_TOKEN is not set");
    let id = env::var("TELEGRAM_CHATID").expect("$TELEGRAM_CHATID is not set");
    let bot = Bot::new(token);
    let chat_id = teloxide::prelude::ChatId(id.parse::<i64>().unwrap());

    for received in rx {
        println!("Got: {}", received);
        bot.send_message(chat_id, received).await.unwrap();
    }
    
}