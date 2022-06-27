import config from "@/config.js";

export async function addNewMessage(name, phone, message) {
    
    const settings = {
      method: "POST",
      body: JSON.stringify(name, phone, message),
      headers: {
        
        "Content-Type": "application/json",
      },
    };
    await fetch(`${config.API_PATH}/messagesList`, settings);
  }
  