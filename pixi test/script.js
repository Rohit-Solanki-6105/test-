class Character {
    constructor(app, x, y) {
        this.sprite = new PIXI.Sprite(PIXI.Texture.from('char.png'));
        this.sprite.anchor.set(0.5);
        this.sprite.x = x;
        this.sprite.y = y;
        this.velocityY = 0;
        this.isJumping = false;
        this.jumpForce = -8;
        this.run_speed = 10;

        app.stage.addChild(this.sprite);

        // life
        this.maxLife = 100;
        this.currentLife = this.maxLife;

        // Create the life bar
        this.lifeBar = new PIXI.Graphics();
        this.lifeBar.x = 30;
        this.lifeBar.y = 30;
        this.updateLifeBar();

        // Blinking variables
        this.blinkDuration = 60; // Set the duration of the blinking in frames
        this.blinkCounter = 0;
        this.isBlinking = false;

        app.stage.addChild(this.lifeBar);
    }

    jump() {
        if (!this.isJumping) {
            this.velocityY = this.jumpForce;
            this.isJumping = true;
        }
    }

    run_forward(){
        this.sprite.x += this.run_speed;
    }

    run_backward(){
        this.sprite.x -= this.run_speed;
    }

    update(platforms, obstacles, enemies) {

        this.velocityY += 0.3; // Gravity

        let onGround = false;

        for (const platform of platforms) {
            if (this.isOnPlatform(platform.getBounds())) {
                // Collision detected, stop falling
                this.velocityY = 0;
                this.isJumping = false;
                this.sprite.y = platform.getBounds().y - this.sprite.height / 2;
                onGround = true;
                break;
            }
        }

        if (!onGround) {
            this.isJumping = true;
        }

        // Update character's position
        this.sprite.y += this.velocityY;

        if(this.sprite.y >= window.innerHeight){
            this.decreaseLife(101);
        }
        
        // obstacles
        for (const obstacle of obstacles) {
            if (this.isCollidingWith(obstacle.getBounds())) {
                this.decreaseLife(0.2); // Adjust the amount to decrease life as needed
                
                // Toggle the blinking effect
                this.isBlinking = true;
                this.blinkCounter = 0;
                
                // Optionally, you may want to remove the obstacle from the stage
                // app.stage.removeChild(obstacle.sprite);
                break;
            }
            else{ 
                this.isBlinking = false;
                this.blinkCounter = 0;
            }
        }

        if (this.isBlinking) {
            this.blinkCounter++;
            if (this.blinkCounter >= this.blinkDuration) {
                this.isBlinking = false;
                this.blinkCounter = 0;
                this.sprite.visible = true; // Make the character visible again
            } else {
                // Toggle visibility every few frames to create blinking effect
                this.sprite.visible = !this.sprite.visible;
            }
        }
        else{
            this.sprite.visible = true;
        }
        // this.lifeBar.x = this.sprite.x - this.sprite.width - 10;
        // this.lifeBar.y = this.sprite.y - this.sprite.height - 50;
    }

    

    isCollidingWith(obstacle) {
        return (
            this.sprite.y + this.sprite.height / 2 > obstacle.y &&
            this.sprite.y - this.sprite.height / 2 < obstacle.y + obstacle.height &&
            this.sprite.x + this.sprite.width / 2 > obstacle.x &&
            this.sprite.x - this.sprite.width / 2 < obstacle.x + obstacle.width
        );
    }

    isOnPlatform(platform) {
        return (
            this.sprite.y + this.sprite.height / 2 > platform.y &&
            this.sprite.y - this.sprite.height / 2 < platform.y + platform.height &&
            this.sprite.x + this.sprite.width / 2 > platform.x &&
            this.sprite.x - this.sprite.width / 2 < platform.x + platform.width
        );
    }

    
    updateLifeBar() {
        const barWidth = 100;
        const barHeight = 10;

        // Clear the previous graphics
        this.lifeBar.clear();

        // this.lifeBar.lineStyle(2, 0x000000); // 2 pixels wide, white color
        // this.lifeBar.drawRect(this.lifeBar.x, this.lifeBar.y, 100, 20);

        // Draw the background of the life bar
        this.lifeBar.beginFill(0x333333); // Dark gray color, you can change it
        this.lifeBar.drawRect(this.lifeBar.x, this.lifeBar.y, barWidth, barHeight);
        this.lifeBar.endFill();

        // Draw the current life
        const lifePercentage = (this.currentLife / this.maxLife) * 100;
        const lifeBarWidth = (lifePercentage / 100) * barWidth;

        this.lifeBar.beginFill(0xFF0000); // Red color, you can change it
        // this.lifeBar.drawRect(this.sprite.x - barWidth / 2, this.sprite.y - 30, lifeBarWidth, barHeight);
        this.lifeBar.drawRect(this.lifeBar.x, this.lifeBar.y, lifeBarWidth, barHeight);
        this.lifeBar.endFill();
        
    }

    decreaseLife(amount) {
        this.currentLife -= amount;

        // Ensure life doesn't go below 0
        if (this.currentLife < 0) {
            this.currentLife = 0;
        }

        this.updateLifeBar();

        // Optionally, add a game over condition when the life reaches 0
        if (this.currentLife <= 0) {
            // Game over logic
            console.log("Game Over!");
            // alert("Game Over!");
            this.gameover();
        }
    }

    gameover(){
        alert("Game Over");
        // this.sprite.x = 100;
    }
    // onside(platforms){
    //     for (const platform of platforms) {
    //         if (this.isOnPlatform(platform.getBounds())) {
    //             // Collision detected, stop falling
    //             if(platform.sprite.x)
    //             break;
    //         }
    //     }
    // }
}

class Platform {// also can be used for ground
    constructor(app, x, y, width) {
        this.sprite = new PIXI.Graphics();
        this.sprite.beginFill(0x996633);
        this.sprite.drawRect(0, 0, width, 20);
        this.sprite.endFill();
        this.sprite.x = x;
        this.sprite.y = y;
        this.width = width;
        this.height = 20;

        app.stage.addChild(this.sprite);
    }

    getBounds() {
        return {
            x: this.sprite.x,
            y: this.sprite.y,
            width: this.width,
            height: this.height,
        };
    }
}

class Cloud {
    constructor(app, img, x, y) {
        this.sprite = new PIXI.Sprite(PIXI.Texture.from(img));
        // this.sprite.anchor.set();
        this.sprite.x = x;
        this.sprite.y = y;
        this.sprite.scale.set(2.3);
        app.stage.addChild(this.sprite);
    }
}

class Obstacle {
    constructor(app, x, y, width, height, imagePath) {
        this.sprite = new PIXI.Sprite(PIXI.Texture.from(imagePath));
        this.sprite.x = x;
        this.sprite.y = y;
        this.sprite.width = width;
        this.sprite.height = height;

        app.stage.addChild(this.sprite);
    }

    getBounds() {
        return {
            x: this.sprite.x,
            y: this.sprite.y,
            width: this.sprite.width,
            height: this.sprite.height,
        };
    }

}

class Knife {
    constructor(app, x, y) {
        this.app = app;
        this.sprite = new PIXI.Sprite(PIXI.Texture.from('knife.webp'));
        this.sprite.anchor.set(0.5);
        this.sprite.x = x;
        this.sprite.y = y;
        this.speed = 10;
        this.isActive = false;
    }

    throwKnife() {
        this.isActive = true;

        // Make the knife visible when thrown
        this.app.stage.addChild(this.sprite);
    }

    update() {
        if (this.isActive) {
            // You can customize the throwing behavior here
            // For simplicity, let's make the knife move continuously
            this.sprite.x += this.speed;

            // Optional: Reset the knife position if it goes off the screen
            if (this.sprite.x > window.innerWidth + this.sprite.width / 2) {
                this.isActive = false;
                this.sprite.x = -this.sprite.width / 2;

                // Remove the knife from the stage when it's not active
                this.app.stage.removeChild(this.sprite);
            }
        }
    }
}


class Enemy {
    constructor(app, x, y, height, width, range, img, canJump = false, movementType = 'forward', gravity = true) {
        this.app = app;
        this.sprite = new PIXI.Sprite(PIXI.Texture.from(img));
        this.sprite.anchor.set(0.5);
        this.sprite.x = x;
        this.sprite.y = y;
        this.sprite.height = height;
        this.sprite.width = width;
        this.speed = 3;
        this.canJump = canJump;
        this.jumpForce = -8;
        this.isJumping = false;
        this.jumpCooldown = Math.random() * 300 + 100; // Random jump cooldown
        this.gravity = gravity;

        // Specify the movement type: 'forward' or 'side'
        this.movementType = movementType;

        // Additional parameters for side movement
        this.sideSpeed = 10;
        this.sideDirection = -1; // Start with a specific direction
        // Additional parameters for continuous forward movement
        this.continuousForwardSpeed = 10;

        this.penX = x; // Set the initial value to the x-coordinate of the enemy
        this.penRange = range;

        
        this.velocityY = 0;

        app.stage.addChild(this.sprite);
    }

    isOnPlatform(platform) {
        return (
            this.sprite.y + this.sprite.height / 2 > platform.y &&
            this.sprite.y - this.sprite.height / 2 < platform.y + platform.height &&
            this.sprite.x + this.sprite.width / 2 > platform.x &&
            this.sprite.x - this.sprite.width / 2 < platform.x + platform.width
        );
    }

    update(platforms) {


        // Move horizontally
        this.sprite.x += this.speed;

        // Optionally, make the enemy jump
        if (this.canJump) {
            this.jumpCooldown--;

            if (this.jumpCooldown <= 0) {
                this.jump();
                this.jumpCooldown = Math.random() * 300 + 100; // Reset jump cooldown
            }
        }
        
        if (this.movementType === 'forward') {
            // Move continuously forward
            this.sprite.x -= this.continuousForwardSpeed;
        } else if (this.movementType === 'side') {
            // Move side by side in a pendulum manner
            this.sprite.x += this.sideSpeed * this.sideDirection;
    
            // Reverse direction when hitting the screen boundary
            if (this.sideDirection === -1 && this.sprite.x <= this.penX - this.penRange) {
                this.sideDirection = 1;
            } else if (this.sideDirection === 1 && this.sprite.x >= this.penX + this.penRange) {
                this.sideDirection = -1;
            }
        }

        if(this.gravity){
            this.velocityY += 0.3;
            // platforms
            for (const platform of platforms) {
                if (this.isOnPlatform(platform.getBounds())) {
                    // Collision detected, stop falling
                    this.velocityY = 0;
                    this.isJumping = false;
                    this.sprite.y = platform.getBounds().y - this.sprite.height / 2;
                    // onGround = true;
                    break;
                }
            }
            
            this.sprite.y += this.velocityY;
        }

        if(this.sprite.y > app.screen.height){
            app.stage.removeChild(this.sprite);
        }
    }

    jump() {
        if (!this.isJumping) {
            this.isJumping = true;
            this.sprite.y += this.jumpForce;
        }
    }

    getBounds() {
        return {
            x: this.sprite.x,
            y: this.sprite.y,
            width: this.width,
            height: this.height,
        };
    }
}

const app = new PIXI.Application({
    width: innerWidth,
    height: innerHeight,
    backgroundColor: 0x1099bb,
});

document.body.appendChild(app.view);


// Load the background image
const backgroundTexture = PIXI.Texture.from('side_fuji5.jpg');
const background = new PIXI.Sprite(backgroundTexture);

// Set the background's position and scale to cover the whole canvas
background.position.set(0, 0);
background.width = app.screen.width * 1.5;
background.height = app.screen.height * 1.2;

app.stage.addChild(background);

//clouds
const clouds = [
    new Cloud(app, "clouds/cloud1.png", 100, 100),
    new Cloud(app, "clouds/cloud2.png", 400, 200),
    new Cloud(app, "clouds/cloud3.png", 200, 300),
    new Cloud(app, "clouds/cloud4.png", 900, 100)
];

const character = new Character(app, 100, 100);

const platforms = [
    new Platform(app, 0, 400, 150),
    new Platform(app, 200, 300, 200),
    new Platform(app, 400, 400, 150),
    new Platform(app, 700, 200, 140),
    new Platform(app, 800, 300, 100),
    new Platform(app, 1000, 450, 200),
    // Add more platforms as needed
];

// const knife = new Knife(app, 100, app.screen.height / 2);

//obstacle 1
const obstacles = [
    new Obstacle(app, 300, 200, 50, 50, 'obstacle1.png'),
    new Obstacle(app, 500, 350, 50, 50, 'obstacle1.png')
];

//knife
const knife = new Knife(app, 100, app.screen.height / 2);

// enimies
const enemies = [
    new Enemy(app, 800, 100, 100, 100, 0, 'e1.png', false, 'forward', false),
    new Enemy(app, 500, 100, 50, 50, 0, 'e1.png', true), // This enemy can jump
    new Enemy(app, 800, 100, 100, 100, 100, 'e1.png', true, 'side'),
    new Enemy(app, 1000, 100, 50, 50, 250, 'e1.png', false, 'side', false)
];

//main loop
app.ticker.add(() => {
    if (character.sprite.x > app.screen.width / 2) {
        // Move the background and platforms in the opposite direction of the character
        const movementSpeed = 10; // Adjust the speed as needed
        background.x -= character.run_speed/8;
        
        platforms.forEach(platform => {
            platform.sprite.x -= character.run_speed;
        });

        clouds.forEach(cloud => {
            cloud.sprite.x -= character.run_speed/7;          
        });

        obstacles.forEach(obs => {
            obs.sprite.x -= character.run_speed;
        })

        enemies.forEach(enemy => {
            enemy.penX -= character.run_speed;
        })

        character.sprite.x = app.screen.width / 2;
    }

    character.update(platforms, obstacles, enemies);
    
    knife.update();

    //for enimies
    for (const enemy of enemies) {
        enemy.update(platforms);

        // Check for collisions with the character
        if (character.isCollidingWith(enemy.sprite.getBounds())) {
            // Handle collision with enemy (e.g., decrease character's life)
            // character.decreaseLife(10);
        }
    }

});


// events
const keys = {};
document.addEventListener('keydown', (event) => {
    keys[event.key] = true;

    
    if(keys['x'] || keys['X']){
        character.run_speed = 20;
    }
    else{
        character.run_speed = 10;
    }
    
    if (keys['ArrowRight'] && (keys[' '] || keys['ArrowUp'])){
        character.run_forward();
        character.jump();
    }
    if (keys['ArrowLeft'] && (keys[' '] || keys['ArrowUp'])){
        character.run_backward();
        character.jump();
    }

    if (keys[' '] || keys['ArrowUp']) {
        character.jump();
    }
    if (keys['ArrowRight']){
        character.run_forward();
    }

    if (keys['ArrowLeft']){
        character.run_backward();
    }


    if (keys['a'] || keys['A']) {
        knife.throwKnife();
    }
});

document.addEventListener('keyup', (event) => {
    keys[event.key] = false;
});
