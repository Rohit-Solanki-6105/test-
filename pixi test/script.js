class Character {
    constructor(app, x, y) {
        this.sprite = new PIXI.Sprite(PIXI.Texture.from('char.png'));
        this.sprite.anchor.set(0.5);
        this.sprite.x = x;
        this.sprite.y = y;
        this.velocityY = 0;
        this.isJumping = false;
        this.jumpForce = -8;

        app.stage.addChild(this.sprite);
    }

    jump() {
        if (!this.isJumping) {
            this.velocityY = this.jumpForce;
            this.isJumping = true;
        }
    }

    run_forward(){
        this.sprite.x += 10;
    }

    run_backward(){
        this.sprite.x -= 10;
    }

    update(platforms) {
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

        // if(this.sprite.y >= window.innerHeight){
        //     alert("Fall");
        //     location.reload();
        // }
    }

    isOnPlatform(platform) {
        return (
            this.sprite.y + this.sprite.height / 2 > platform.y &&
            this.sprite.y - this.sprite.height / 2 < platform.y + platform.height &&
            this.sprite.x + this.sprite.width / 2 > platform.x &&
            this.sprite.x - this.sprite.width / 2 < platform.x + platform.width
        );
    }
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

app.ticker.add(() => {
    if (character.sprite.x > app.screen.width / 2) {
        // Move the background and platforms in the opposite direction of the character
        const movementSpeed = 10; // Adjust the speed as needed
        background.x -= 0.4;
        platforms.forEach(platform => {
            platform.sprite.x -= movementSpeed;
        });
        character.sprite.x = app.screen.width / 2;
    }

    character.update(platforms);
});


// events
const keys = {};
document.addEventListener('keydown', (event) => {
    keys[event.key] = true;

    
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
        console.log(keys);
    }
    if (keys['ArrowRight']){
        character.run_forward();
        console.log(keys);
    }

    if (keys['ArrowLeft']){
        character.run_backward();
        console.log(keys);
    }
});

document.addEventListener('keyup', (event) => {
    keys[event.key] = false;
});