import config from "@/config.js";

export async function admin(user, password) {
    const settings = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            user: user,
            password: password,
        }),

    };

    
    const response = await fetch(`${config.AUTH_PATH}/admin`, settings);
    return response
}

