class Character {
    constructor(app, x, y) {
        this.sprite = new PIXI.Sprite(PIXI.Texture.from('transparent.png'));
        this.sprite.anchor.set(0.5);
        this.sprite.x = x;
        this.sprite.y = y;
        this.sprite.height = 100;
        this.sprite.width = 90;
        this.velocityY = 0;
        this.isJumping = false;
        this.jumpForce = -14;
        this.run_speed = 10;
        this.starCount = 0;
        this.AttackPower = 0;

        app.stage.addChild(this.sprite);

        // life
        this.maxLife = 100;
        this.currentLife = this.maxLife;

        // Create the life bar
        this.lifeBar = new PIXI.Graphics();
        this.lifeBar.x = 30;
        this.lifeBar.y = 30;
        this.lifeNumber = 3;

        // Create the life number text
        this.lifeNumberText = new PIXI.Text(`X ${this.lifeNumber}`, { fontSize: 20, fill: 0x000000 });
        this.lifeNumberText.x = 30; // Adjust the position
        this.lifeNumberText.y = 30;
        this.updateLifeBar();


        // Blinking variables
        this.blinkDuration = 60; // Set the duration of the blinking in frames
        this.blinkCounter = 0;
        this.isBlinking = false;

        // default knifes numbers
        this.knifeCount = 0;
        // for(let i=0; i<)

        app.stage.addChild(this.lifeBar);
        
        app.stage.addChild(this.lifeNumberText);

        this.StarText = new PIXI.Text(`x ${this.starCount}`, {
            fontSize: 25,
            fill: 0x000000,
            align: 'center'
        });

        this.StarText.x = 90;
        this.StarText.y = 80;
        
        app.stage.addChild(this.StarText);

        this.knifeText = new PIXI.Text(`x ${this.knifeCount}`, {
            fontSize: 25,
            fill: 0x000000,
            align: 'center'
        });

        this.knifeText.x = 90;
        this.knifeText.y = 120;
        
        app.stage.addChild(this.knifeText);



        //------------------ animations---------------------

        // ----------run-----------
        this.Rw = 363;
        this.Rh = 450;
        
        this.runTexture = new PIXI.BaseTexture.from('character_sprites/running_frames.png');
        this.RunImages = [
            new PIXI.Texture(this.runTexture, new PIXI.Rectangle(0 * this.Rw, 0, this.Rw, this.Rh)),
            new PIXI.Texture(this.runTexture, new PIXI.Rectangle(1 * this.Rw, 0, this.Rw, this.Rh)),
            new PIXI.Texture(this.runTexture, new PIXI.Rectangle(2 * this.Rw, 0, this.Rw, this.Rh)),
            new PIXI.Texture(this.runTexture, new PIXI.Rectangle(3 * this.Rw, 0, this.Rw, this.Rh)),
            new PIXI.Texture(this.runTexture, new PIXI.Rectangle(4 * this.Rw, 0, this.Rw, this.Rh)),
            new PIXI.Texture(this.runTexture, new PIXI.Rectangle(5 * this.Rw, 0, this.Rw, this.Rh)),
            new PIXI.Texture(this.runTexture, new PIXI.Rectangle(6 * this.Rw, 0, this.Rw, this.Rh)),
            new PIXI.Texture(this.runTexture, new PIXI.Rectangle(7 * this.Rw, 0, this.Rw, this.Rh)),
            new PIXI.Texture(this.runTexture, new PIXI.Rectangle(8 * this.Rw, 0, this.Rw, this.Rh)),
            new PIXI.Texture(this.runTexture, new PIXI.Rectangle(9 * this.Rw, 0, this.Rw, this.Rh)),
        ];
        
        this.RunSprite = new PIXI.AnimatedSprite(this.RunImages);
        this.isRunning = false;

        //---------------- stand -------------------
        this.Sh = 439;
        this.Sw = 232;

        this.standTexture = new PIXI.BaseTexture.from('character_sprites/standing_frames.png');
        this.StandImages = [
            new PIXI.Texture(this.standTexture, new PIXI.Rectangle(0 * this.Sw, 0, this.Sw, this.Sh)),
            new PIXI.Texture(this.standTexture, new PIXI.Rectangle(1 * this.Sw, 0, this.Sw, this.Sh)),
            new PIXI.Texture(this.standTexture, new PIXI.Rectangle(2 * this.Sw, 0, this.Sw, this.Sh)),
            new PIXI.Texture(this.standTexture, new PIXI.Rectangle(3 * this.Sw, 0, this.Sw, this.Sh)),
            new PIXI.Texture(this.standTexture, new PIXI.Rectangle(4 * this.Sw, 0, this.Sw, this.Sh)),
            new PIXI.Texture(this.standTexture, new PIXI.Rectangle(5 * this.Sw, 0, this.Sw, this.Sh)),
            new PIXI.Texture(this.standTexture, new PIXI.Rectangle(6 * this.Sw, 0, this.Sw, this.Sh)),
            new PIXI.Texture(this.standTexture, new PIXI.Rectangle(7 * this.Sw, 0, this.Sw, this.Sh)),
            new PIXI.Texture(this.standTexture, new PIXI.Rectangle(8 * this.Sw, 0, this.Sw, this.Sh)),
            new PIXI.Texture(this.standTexture, new PIXI.Rectangle(9 * this.Sw, 0, this.Sw, this.Sh)),
        ];

        this.StandSprite = new PIXI.AnimatedSprite(this.StandImages);
        this.isStanding = true;

        //--------jumping--------------
        this.Jh = 445;
        this.Jw = 362;

        this.jumpTexture = new PIXI.BaseTexture.from('character_sprites/jumping_frames.png');
        this.JumpImages = [
            new PIXI.Texture(this.jumpTexture, new PIXI.Rectangle(0 * this.Jw, 0, this.Jw, this.Jh)),
            new PIXI.Texture(this.jumpTexture, new PIXI.Rectangle(1 * this.Jw, 0, this.Jw, this.Jh)),
            new PIXI.Texture(this.jumpTexture, new PIXI.Rectangle(2 * this.Jw, 0, this.Jw, this.Jh)),
            new PIXI.Texture(this.jumpTexture, new PIXI.Rectangle(3 * this.Jw, 0, this.Jw, this.Jh)),
            new PIXI.Texture(this.jumpTexture, new PIXI.Rectangle(4 * this.Jw, 0, this.Jw, this.Jh)),
            new PIXI.Texture(this.jumpTexture, new PIXI.Rectangle(5 * this.Jw, 0, this.Jw, this.Jh)),
            new PIXI.Texture(this.jumpTexture, new PIXI.Rectangle(6 * this.Jw, 0, this.Jw, this.Jh)),
            new PIXI.Texture(this.jumpTexture, new PIXI.Rectangle(7 * this.Jw, 0, this.Jw, this.Jh)),
            new PIXI.Texture(this.jumpTexture, new PIXI.Rectangle(8 * this.Jw, 0, this.Jw, this.Jh)),
            new PIXI.Texture(this.jumpTexture, new PIXI.Rectangle(9 * this.Jw, 0, this.Jw, this.Jh)),
        ];

        this.JumpSprite = new PIXI.AnimatedSprite(this.JumpImages);
        this.jumping = false;

        //------------- throw knife ------------------
        // this.Th = 445;
        // this.Tw = 373;

        // this.throwTexture = new PIXI.BaseTexture.from('character_sprites/throwing_frames.png');
        // this.ThrowImages = [
        //     new PIXI.Texture(this.throwTexture, new PIXI.Rectangle(0 * this.Tw, 0, this.Tw, this.Th)),
        //     new PIXI.Texture(this.throwTexture, new PIXI.Rectangle(1 * this.Tw, 0, this.Tw, this.Th)),
        //     new PIXI.Texture(this.throwTexture, new PIXI.Rectangle(2 * this.Tw, 0, this.Tw, this.Th)),
        //     new PIXI.Texture(this.throwTexture, new PIXI.Rectangle(3 * this.Tw, 0, this.Tw, this.Th)),
        //     new PIXI.Texture(this.throwTexture, new PIXI.Rectangle(4 * this.Tw, 0, this.Tw, this.Th)),
        //     new PIXI.Texture(this.throwTexture, new PIXI.Rectangle(5 * this.Tw, 0, this.Tw, this.Th)),
        //     new PIXI.Texture(this.throwTexture, new PIXI.Rectangle(6 * this.Tw, 0, this.Tw, this.Th)),
        //     new PIXI.Texture(this.throwTexture, new PIXI.Rectangle(7 * this.Tw, 0, this.Tw, this.Th)),
        //     new PIXI.Texture(this.throwTexture, new PIXI.Rectangle(8 * this.Tw, 0, this.Tw, this.Th)),
        //     new PIXI.Texture(this.throwTexture, new PIXI.Rectangle(9 * this.Tw, 0, this.Tw, this.Th)),
        // ];

        // this.ThrowSprite = new PIXI.AnimatedSprite(this.ThrowImages);
        // this.isThrowing = false;
        // this.jumping = false;
        
        // -------- sprite for current animation --------
        this.CurrentAnimation = this.StandSprite;
        this.CurrentAnimation.animationSpeed = 0.3;
        this.CurrentAnimation.loop = true;
        // RunSprite.x = this.x;
        // RunSprite.y = this.y;
        this.CurrentAnimation.x = this.sprite.x;
        this.CurrentAnimation.y = this.sprite.y;
        this.CurrentAnimation.height = this.sprite.height;
        this.CurrentAnimation.width = this.sprite.width;

        
        this.CurrentAnimation.anchor.set(0.5);

        app.stage.addChild(this.CurrentAnimation);
        this.CurrentAnimation.loop = true;
        this.CurrentAnimation.play();
        // this.RunSprite.visibile = false;

    }

    jump() {
        if (!this.isJumping) {
            this.velocityY = this.jumpForce;
            this.isJumping = true;
        }
    }

    run_forward(){
        // this.CurrentAnimation.scale.x = 1;
        this.CurrentAnimation.scale.x = 0.35;
        this.sprite.x += this.run_speed;
    }

    run_backward(){
        // this.CurrentAnimation.scale.x = -1;
        this.CurrentAnimation.scale.x = -0.35;
        this.sprite.x -= this.run_speed;
    }

    update(platforms, obstacles, enemies, bricks, collectors) {

        this.velocityY += 0.3; // Gravity

        let onGround = false;

        this.CurrentAnimation.x = this.sprite.x;
        this.CurrentAnimation.y = this.sprite.y;
        // this.RunSprite.height = this.sprite.height;
        // this.RunSprite.width = this.sprite.width;

        for (const platform of platforms) {
            if (this.isOnPlatform(platform.getBounds())) {
                // Collision detected, stop falling
                this.velocityY = 0;
                this.isJumping = false;
                this.jumping = false;
                this.sprite.y = platform.getBounds().y - this.sprite.height / 2;
                onGround = true;
                // this.isStanding = true;
                break;
            }
        }

        if (!onGround) {
            this.isJumping = true;
            this.velocityY+=0.3;
        }

        // Update character's position
        this.sprite.y += this.velocityY;

        if(this.sprite.y >= window.innerHeight){
            this.decreaseLife(101);
        }
        
        // obstacles
        for (const obstacle of obstacles) {
            if (this.isCollidingWith(obstacle.getBounds())) {
                this.decreaseLife(obstacle.lifeDecrease); // Adjust the amount to decrease life as needed
                
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

        for (const enemy of enemies) {
            if (this.sprite.x+this.sprite.width/2 >= enemy.sprite.x && // right
            this.sprite.x-this.sprite.width/2 <= enemy.sprite.x+enemy.sprite.width && //left
            this.sprite.y+this.sprite.height/2 >= enemy.sprite.y && //top
            this.sprite.y-this.sprite.height/2 <= enemy.sprite.y+enemy.sprite.height/2) {
                this.decreaseLife(enemy.lifeDecrease); // Adjust the amount to decrease life as needed
                // alert("hi")
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
                this.CurrentAnimation.visibile = true;
            } else {
                // Toggle visibility every few frames to create blinking effect
                this.sprite.visible = !this.sprite.visible;
                this.CurrentAnimation.visible = !this.CurrentAnimation.visible;
            }
        }
        else{
            this.sprite.visible = true;
            this.CurrentAnimation.visible = true;
        }
        // this.lifeBar.x = this.sprite.x - this.sprite.width - 10;
        // this.lifeBar.y = this.sprite.y - this.sprite.height - 50;


        for (let i=0; i< bricks.length; i++) {
            const brick = bricks[i];

            if(this.sprite.x+this.sprite.width/2 >= brick.sprite.x && // right
            this.sprite.x-this.sprite.width/2 <= brick.sprite.x+brick.sprite.width && //left
            this.sprite.y+this.sprite.height/2 >= brick.sprite.y && //top
            this.sprite.y-this.sprite.height/2 <= brick.sprite.y+brick.sprite.height/2 // bottom
                ){
                if(brick.canBreak){
                    // setTimeout(()=>{
                        app.stage.removeChild(brick.sprite);
                        bricks.splice(i, 1);
                    // }, brick.afterTime);
                }
                    // alert(true)
                
                if(this.sprite.y+this.sprite.height/2 > brick.sprite.y+2 && 
                this.sprite.y+this.sprite.height/2 < brick.sprite.y+brick.sprite.height/2){ // top
                    this.velocityY = 0;
                    this.sprite.y = brick.sprite.y-(this.sprite.height/2);
                    onGround = true;
                    this.isJumping = false;
                    this.jumping = false;
                }

                if(this.sprite.y-this.sprite.height <= brick.sprite.y+brick.sprite.height){//bottom
                    this.velocityY = 3;
                }

                if(this.sprite.y > brick.sprite.y && 
                    this.sprite.x+this.sprite.width/2 > brick.sprite.x-2 && 
                    this.sprite.x+this.sprite.width/2 <= brick.sprite.x+5){ // left
                    // this.run_speed = 0;
                    this.sprite.x = brick.sprite.x-(this.sprite.width/2)-5;
                }

                if(this.sprite.y > brick.sprite.y && 
                    this.sprite.x <= brick.sprite.x+brick.sprite.width+20 && 
                    this.sprite.x >= brick.sprite.x+brick.sprite.width-20){ // right
                    // this.run_speed = 0;
                    this.sprite.x = brick.sprite.x+(brick.sprite.width/2)+(this.sprite.width)+2;
                }
                
                // this.velocityY = 0;
            }
        }

        for (let i=0; i< collectors.length; i++) {
            const collect = collectors[i];

            if(this.sprite.x+this.sprite.width/2 >= collect.sprite.x && // right
            this.sprite.x-this.sprite.width/2 <= collect.sprite.x+collect.sprite.width && //left
            this.sprite.y+this.sprite.height/2 >= collect.sprite.y && //top
            this.sprite.y-this.sprite.height/2 <= collect.sprite.y+collect.sprite.height/2 // bottom
                ){
                    collect.action(this);
                    app.stage.removeChild(collect.sprite);
                    collectors.splice(i, 1);
                    break;
                // this.velocityY = 0;
            }
        }
        this.starShow();
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
        
        this.lifeNumberText.text = `X ${this.lifeNumber}`;
        // this.lifeNumberText = new PIXI.Text(`X ${this.lifeNumber}`, { fontSize: 20, fill: 0x000000 });
        this.lifeNumberText.y = this.lifeBar.y + barHeight + 10;
        this.lifeNumberText.x = this.lifeBar.x + 150;

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
        // if (this.currentLife < 0) {
        //     this.currentLife = 0;
        // }


        if (this.currentLife <= 0 && this.lifeNumber > 0) {
            this.lifeNumber--;
    
            if (this.lifeNumber > 0) {
                this.sprite.x = levels[level].character_init_position.x;
                this.sprite.y = levels[level].character_init_position.y;
                // Player has more lives left
                // Create a black overlay
                const blackOverlay = new PIXI.Graphics();
                blackOverlay.beginFill(0x000000);
                blackOverlay.drawRect(0, 0, app.screen.width, app.screen.height);
                blackOverlay.endFill();
                app.stage.addChild(blackOverlay);

                // Hide the character during the black screen
                this.sprite.visible = false;

                // Display the number of remaining lives
                const lifeText = new PIXI.Text(`Remaining Lives: ${this.lifeNumber}`, {
                    fontSize: 30,
                    fill: 0xFFFFFF,
                    align: 'center'
                });
                lifeText.x = app.screen.width / 2 - lifeText.width / 2;
                lifeText.y = app.screen.height / 2 - lifeText.height / 2;
                app.stage.addChild(lifeText);

                // Wait for 2 seconds (adjust the duration as needed)
                setTimeout(() => {
                    // Remove the black overlay and life text
                    app.stage.removeChild(blackOverlay);
                    app.stage.removeChild(lifeText);
                    blackOverlay.visibile = false;
                    lifeText.visibile = false;

                    // Make the character visible again
                    this.sprite.visible = true;
                    this.sprite.x = 100;
                }, 1000); // 2000 milliseconds = 2 seconds
                    
                // Player has more lives left
                this.sprite.y = 100;
                this.currentLife = 100;
    
                // Update the life number text
                this.lifeNumberText.text = `X ${this.lifeNumber}`;
            } else {
                // No more lives, trigger game over
                this.gameover();
            }
        }

        
        this.updateLifeBar();
    }

    gameover() {
        // Create a black overlay
        const blackOverlay = new PIXI.Graphics();
        blackOverlay.beginFill(0x000000);
        blackOverlay.drawRect(0, 0, app.screen.width, app.screen.height);
        blackOverlay.endFill();
        app.stage.addChild(blackOverlay);
    
        // Display the number of remaining lives
        const gameOverText = new PIXI.Text(`Game Over\nRemaining Lives: ${this.lifeNumber}`, {
            fontSize: 30,
            fill: 0xFFFFFF,
            align: 'center'
        });
        gameOverText.x = app.screen.width / 2 - gameOverText.width / 2;
        gameOverText.y = app.screen.height / 2 - gameOverText.height / 2;
        app.stage.addChild(gameOverText);
    }

    // throwKnife() {
    //     if(this.knifeCount > 0){
    //         if(!this.isThrowing){
    //             this.isThrowing = true;
    //             this.CurrentAnimation.textures = character.ThrowImages;
    //             this.CurrentAnimation.loop = false;
    //             this.CurrentAnimation.play();
    //         }
    //     }
    // }

    starShow(){
        const starDisplay = new PIXI.Sprite(PIXI.Texture.from('star.png'));
        starDisplay.x = 50;
        starDisplay.y = 80;
        starDisplay.width = 30;
        starDisplay.height = 30;

        app.stage.addChild(starDisplay);

        this.StarText.text = `x ${this.starCount}`;

        const knifeDisplay = new PIXI.Sprite(PIXI.Texture.from('knife.png'));
        knifeDisplay.x = 50;
        knifeDisplay.y = 120;
        knifeDisplay.width = 30;
        knifeDisplay.height = 30;

        app.stage.addChild(knifeDisplay);

        this.knifeText.text = `x ${this.knifeCount}`;
        
        // console.log(this.StarText);

        // this.StarText = new PIXI.Text(`x ${this.starCount}`, {
        //     fontSize: 30,
        //     fill: 0x000000,
        //     align: 'center'
        // });

        // StarText.x = app.screen.width / 2 - lifeText.width / 2;
        // StarText.y = app.screen.height / 2 - lifeText.height / 2;
        // app.stage.addChild(StarText);
    }
}

class Platform {// also can be used for ground
    constructor(app, x, y, height, width, img) {
        this.sprite = new PIXI.Sprite(PIXI.Texture.from(img));
        this.sprite.x = x;
        this.sprite.y = y;
        this.sprite.width = width;
        this.sprite.height = height;
        this.width = width;
        this.height = height;

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
    constructor(app, x, y, width, height, imagePath, lifeDecrease = 0.2) {
        this.sprite = new PIXI.Sprite(PIXI.Texture.from(imagePath));
        this.sprite.x = x;
        this.sprite.y = y;
        this.sprite.width = width;
        this.sprite.height = height;
        this.lifeDecrease = lifeDecrease;

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
    constructor(app) {
        this.app = app;
        this.sprite = new PIXI.Sprite(PIXI.Texture.from('knife.png'));
        this.sprite.anchor.set(0.5);
        this.sprite.x = 0;
        this.sprite.y = 0;
        this.sprite.height = 15;
        this.sprite.width = 70;
        this.speed = 10;
        this.isActive = false;
    }

    throwKnife() {
        this.isActive = true;
        character.AttackPower = 50;

        // Make the knife visible when thrown
        this.app.stage.addChild(this.sprite);
    }

    update(enemies) {
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
        // else{
        //     this.sprite.visibile = false;
        // }

        for (let i=0; i<enemies.length; i++) {
            const enemy = enemies[i];
            if (this.sprite.x+this.sprite.width/2 >= enemy.sprite.x && // right
            this.sprite.x-this.sprite.width/2 <= enemy.sprite.x+enemy.sprite.width && //left
            this.sprite.y+this.sprite.height/2 >= enemy.sprite.y && //top
            this.sprite.y-this.sprite.height/2 <= enemy.sprite.y+enemy.sprite.height/2) {
                enemy.health -= character.AttackPower;
                if(enemy.health <= 0){
                    app.stage.removeChild(enemy.sprite);
                    enemies.splice(i, 1);
                    // Optionally, you may want to remove the obstacle from the stage
                    // app.stage.removeChild(obstacle.sprite);
                    break;
                }
                
                this.isActive = false;
                this.sprite.x = 0;
                this.sprite.y = 0;
                app.stage.removeChild(this.sprite);
            }
        }
    }
}

class Background{
    constructor(app, width_scale, img){
        this.sprite = new PIXI.Sprite(PIXI.Texture.from(img));
        // this.sprite.anchor.set(0.5);
        this.sprite.x = 0;
        this.sprite.y = 0;
        // this.position.set(0, 0);
        this.sprite.width = app.screen.width * width_scale;
        this.sprite.height = app.screen.height * 1.2;

        app.stage.addChild(this.sprite);
        // // Load the background image
        // const backgroundTexture = PIXI.Texture.from(img);
        // const background = new PIXI.Sprite(backgroundTexture);

        // // Set the background's position and scale to cover the whole canvas
        
        // background.width = app.screen.width * width_scale;
        // background.height = app.screen.height * 1.2;

        // app.stage.addChild(background);
    }
}

class Enemy {
    constructor(app, x, y, height, width, range, img, canJump = false, movementType = 'forward', gravity = true, lifeDecrease = 3, health = 25, side_forward_speed = 6) {
        this.app = app;
        this.sprite = new PIXI.Sprite(PIXI.Texture.from(img));
        this.sprite.anchor.set(0.5);
        this.sprite.x = x;
        this.sprite.y = y;
        this.sprite.height = height;
        this.sprite.width = width;
        this.speed = 3;
        this.canJump = canJump;
        this.jumpForce = Math.random() * (-10) + (-5);
        this.isJumping = false;
        this.jumpCooldown = Math.random() * 300 + 100; // Random jump cooldown
        this.gravity = gravity;
        this.lifeDecrease = lifeDecrease;

        this.health = health;

        // Specify the movement type: 'forward' or 'side'
        this.movementType = movementType;
        this.side_forward_speed = side_forward_speed;

        // Additional parameters for side movement
        this.sideSpeed = this.side_forward_speed;
        this.sideDirection = -1; // Start with a specific direction
        // Additional parameters for continuous forward movement
        this.continuousForwardSpeed = this.side_forward_speed;

        this.penX = x; // Set the initial value to the x-coordinate of the enemy
        this.penRange = range;

        this.HealthText = new PIXI.Text('', {
            fontSize: 20,
            fill: 0x000000,
            align: 'center'
        });

        this.HealthText.x = this.sprite.x + this.sprite.width;
        this.HealthText.y = this.sprite.y;

        // this.HealthText.anchor.set(-1, 1)

        app.stage.addChild(this.HealthText);
        
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

    update(platforms, bricks) {
        // health
        this.HealthText.x = this.sprite.x + this.sprite.width / 2;
        this.HealthText.y = this.sprite.y - this.sprite.height / 2;

        this.HealthText.text = this.health;

        // Optionally, make the enemy jump
        if (this.canJump) {
            // this.jumpCooldown--;
            
            this.jump();
            this.velocityY+=0.2;
            // if (this.jumpCooldown <= 0) {
            // this.jumpCooldown = Math.random() * 300 + 100; // Reset jump cooldown
            // }
        }
        
        if(this.sprite.x <= this.app.screen.width){
            this.continuousForwardSpeed = this.side_forward_speed;
            this.sideSpeed = this.side_forward_speed;
        }
        else{
            this.continuousForwardSpeed = 0;
            this.sideSpeed = 0;
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

        for (let i=0; i< bricks.length; i++) {
            const brick = bricks[i];

            if(this.sprite.x+this.sprite.width/2 >= brick.sprite.x && // right
            this.sprite.x-this.sprite.width/2 <= brick.sprite.x+brick.sprite.width && //left
            this.sprite.y+this.sprite.height/2 >= brick.sprite.y && //top
            this.sprite.y-this.sprite.height/2 <= brick.sprite.y+brick.sprite.height/2 // bottom
                ){
                
                if(this.sprite.y+this.sprite.height/2 > brick.sprite.y+2 && 
                this.sprite.y+this.sprite.height/2 < brick.sprite.y+brick.sprite.height/2){ // top
                    this.velocityY = 0;
                    this.sprite.y = brick.sprite.y-(this.sprite.height/2);
                    // onGround = true;
                    this.isJumping = false;
                    this.jumping = false;
                }

                if(this.sprite.y-this.sprite.height <= brick.sprite.y+brick.sprite.height){//bottom
                    this.velocityY = 3;
                }

                if(this.sprite.y > brick.sprite.y && 
                    this.sprite.x+this.sprite.width/2 > brick.sprite.x-2 && 
                    this.sprite.x+this.sprite.width/2 <= brick.sprite.x+5){ // left
                    // this.run_speed = 0;
                    this.sprite.x = brick.sprite.x-(this.sprite.width/2)-5;
                    this.continuousForwardSpeed *= -1;
                    this.sideDirection *= -1;
                }

                if(this.sprite.y > brick.sprite.y && 
                    this.sprite.x <= brick.sprite.x+brick.sprite.width+20 && 
                    this.sprite.x >= brick.sprite.x+brick.sprite.width-20){ // right
                    // this.run_speed = 0;
                    this.sprite.x = brick.sprite.x+(brick.sprite.width/2)+(this.sprite.width)+2;
                    this.continuousForwardSpeed *= -1;
                    this.sideDirection *= -1;
                }
                
                // this.velocityY = 0;
            }
        }
        

    }

    jump() {
        if (!this.isJumping) {
            this.isJumping = true;
            // this.sprite.y += this.jumpForce;
            this.velocityY = this.jumpForce;
        }
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

class Brick {// also can be used for ground
    constructor(app, x, y, height, width, img, breakable = false, afterTime = 0) {
        this.sprite = new PIXI.Sprite(PIXI.Texture.from(img));
        this.sprite.x = x;
        this.sprite.y = y;
        this.sprite.width = width;
        this.sprite.height = height;
        this.afterTime = afterTime;
        // this.height = 20;
        this.canBreak = breakable;

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

class Collector{
    constructor(app, x, y, height, width, name, img){
        this.sprite = new PIXI.Sprite(PIXI.Texture.from(img));
        this.sprite.x = x;
        this.sprite.y = y;
        this.sprite.width = width;
        this.sprite.height = height;
        this.name = name;

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

    action(character){
        if(this.name == 'Life'){
            character.lifeNumber++;
        }
        if(this.name == 'health'){
            character.decreaseLife(-20);
        }

        if(this.name == 'knife'){
            character.knifeCount++;
        }

        if(this.name == 'star'){
            character.starCount++;
        }
    }
}

const app = new PIXI.Application({
    width: innerWidth,
    height: innerHeight,
    backgroundColor: 0x000000,
});

document.body.appendChild(app.view);


let level = 1;
const levels = {
    1:{
        endLevel: 200,

        background: new Background(app, 1.5, 'side_fuji5.jpg'),
        
        clouds: [
            new Cloud(app, "clouds/cloud1.png", 100, 100),
            new Cloud(app, "clouds/cloud2.png", 400, 200),
            new Cloud(app, "clouds/cloud3.png", 200, 300),
            new Cloud(app, "clouds/cloud4.png", 900, 100)
        ],

        platforms: [
                       ///  (app, length position,width position,length size width size)
            new Platform(app,  10,  200,20, 150,'plat.png'),//top 1st 
            new Platform(app, 300,  200,20, 250,'plat.png'),//top 2nd
            new Platform(app, 2600, 590,20, 300,'plat.png'),//top 3rd
            new Platform(app, 650,  320,20, 200,'plat.png'),//mid 1st
            new Platform(app, 900,  500,20, 200, 'plat.png'),//mid 2st
            new Platform(app,1800,  460,20, 250,'plat.png'),//mid 3rd
            new Platform(app,2200,  310,20, 150,'plat.png'),//mid 4th
            new Platform(app,  10,  600,20, 240,'plat.png'),//bottom 1st
            new Platform(app, 400,  600,20, 200,'plat.png'),//bottom 2nd
            new Platform(app,1300,  600,20, 400,'plat.png'),//bottom 3rd
            // new Platform(app, 0, app.screen.height-50, 20, app.screen.width*2, 'plat.png')
            // Add more platforms as needed
        ],

        obstacles: [
            new Obstacle(app, 395, 150, 50, 50, 'obstacle1.png',0.1),
            new Obstacle(app, 2700, 539, 50, 50, 'obstacle1.png')
        ],
        
        enemies: [
             new Enemy(app, 1465, 550, 100, 100, 60, 'e1.png', true, 'side', true,0.2, 100),
            // new Enemy(app, 2200, 100, 50, 50, 200, 'e1.png', true, 'side', true), // This enemy can jump
            // new Enemy(app, 2500, 100, 100, 100, 100, 'e1.png', true, 'forward'),
            // new Enemy(app, 1000, 100, 50, 50, 250, 'e1.png', false, 'side', false),
            // new Enemy(app, 1800, 100, 100, 100, 300, 'e1.png', false, 'side', false),
            // new Enemy(app, 1900, 100, 100, 100, 100, 'e1.png', false, 'side', true)
        ],

        bricks: [
            new Brick(app,   180,   200,20,  100,'brick.png',true,500),
             new Brick(app, 270,    600, 20, 100, 'brick.png', true,500),
            // new Brick(app, 150, 600, 20, 50, 'brick.png', false),
            // new Brick(app, 150, 600, 20, 150, 'brick.png', true, 2000),
            // new Brick(app, 150, 300, 20, 150, 'brick.png', true, 500),
            // new Brick(app, 1000, 600, 20, 150, 'brick.png', false, 500),
            // new Brick(app, 900, 600, 20, 150, 'brick.png', false, 500),
            // // new Brick(app, 1200, 300, 20, 150, 'brick.png', false, 0)
        ],

        collectors: [
            new Collector(app, 490, 300, 30, 30, "knife", "knife.png"),
            new Collector(app, 50, 160, 30, 30, "Life", "life.png"),
            new Collector(app, 1000, 250, 30, 30, "health", "health.png"),
            new Collector(app, 2500, 400, 30, 30, "star", "star.png"),
            new Collector(app, 700,  400,30, 30,"star",'star.png'),//mid 1st)
        ],

        character_init_position:{
            x: 10,
            y: 600
        },

        min_stars: 2

    },

    2:{
        endLevel: 200,
        
        background: new Background(app, 1.5, 'side_fuji5.jpg'),
        
        clouds: [
            new Cloud(app, "clouds/cloud1.png", 100, 100),
            new Cloud(app, "clouds/cloud2.png", 400, 200),
            new Cloud(app, "clouds/cloud3.png", 200, 300),
            new Cloud(app, "clouds/cloud4.png", 900, 100)
        ],

        platforms: [
            new Platform(app,    0, 710, 30, 160, 'plat.png'),//bottom1st
            new Platform(app,  340, 650,90,70,'plat.png'),//pillar 1
            new Platform(app,  590, 550,200,70,'plat.png'),//pillar 2
            new Platform(app,  870, 440,300,70,'plat.png'),//pillar3
            new Platform(app, 1150, 380,380,70,'plat.png'),//pillar4
            new Platform(app, 1450, 480,330,70,'plat.png'),//pillar5
            new Platform(app, 1780,390,400,70,'plat.png'),//pillar6
            new Platform(app, 2100,310,430,70,'plat.png'),//pillar7
            new Platform(app, 2450,270,460,70,'plat.png'),//pillar8
            new Platform(app, 2800,220,510,70,'plat.png'),//pillar9
            new Platform(app, 4100,630,100,70,'plat.png'),//pillar10
            new Platform(app, 4350,550,190,70,'plat.png'),//pillar11
            new Platform(app, 4600,440,300,70,'plat.png'),//pillar12
            new Platform(app, 4900,310,440,70,'plat.png'),//pillar13
            new Platform(app, 3300,710,20,600,'plat.png'),//bottom2nd
            new Platform(app, 5200,350,20,1000,'plat.png'),//bottom3rd
            // Add more platforms as needed
        ],

        obstacles: [
            new Obstacle(app, 300, 200, 50, 50, 'obstacle1.png'),
            new Obstacle(app, 500, 350, 50, 50, 'obstacle1.png')
        ],

        enemies: [
            new Enemy(app, 1600, 100, 100, 100, 0, 'e1.png', false, 'forward', false),
            new Enemy(app, 500, 100, 50, 50, 0, 'e1.png', true), // This enemy can jump
            new Enemy(app, 800, 100, 100, 100, 100, 'e1.png', true, 'side'),
            new Enemy(app, 1000, 100, 50, 50, 250, 'e1.png', false, 'side', false),
            new Enemy(app, 1800, 100, 100, 100, 300, 'e1.png', false, 'side', false),
            new Enemy(app, 1900, 100, 100, 100, 100, 'e1.png', false, 'side', true)
        ],

        bricks: [
            new Brick(app, 100, 200, 20, 100, 'brick.png', false),
            new Brick(app, 300, 200, 20, 100, 'brick.png', true),
            new Brick(app, 500, 500, 30, 100, 'brick.png', false)
        ],
        
        collectors: [
            new Collector(app, 400, 400, 30, 30, "knife", "knife.png"),
            new Collector(app, 500, 500, 30, 30, "Life", "life.png"),
            new Collector(app, 600, 600, 30, 30, "health", "health.png"),
            new Collector(app, 800, 400, 30, 30, "star", "star.png")
        ],

        character_init_position: {
            x: 100,
            y: 100
        },

        min_stars: 2
    }
}

function change_level(){
    if(level <= finalLevel){

        const blackOverlay = new PIXI.Graphics();
        blackOverlay.beginFill(0x000000);
        blackOverlay.drawRect(0, 0, app.screen.width, app.screen.height);
        blackOverlay.endFill();
        app.stage.addChild(blackOverlay);

        // Display the number of remaining lives
        const lifeText = new PIXI.Text(`Level: ${level}`, {
            fontSize: 30,
            fill: 0xFFFFFF,
            align: 'center'
        });
        lifeText.x = app.screen.width / 2 - lifeText.width / 2;
        lifeText.y = app.screen.height / 2 - lifeText.height / 2;
        app.stage.addChild(lifeText);

        // Wait for 2 seconds (adjust the duration as needed)
        setTimeout(() => {
            // Remove the black overlay and life text
            app.stage.removeChild(blackOverlay);
            app.stage.removeChild(lifeText);

            // Make the character visible again
            // this.sprite.visible = true;
            // this.sprite.x = 100;
        }, 2000);
    }
    else{
        const blackOverlay = new PIXI.Graphics();
        blackOverlay.beginFill(0x000000);
        blackOverlay.drawRect(0, 0, app.screen.width, app.screen.height);
        blackOverlay.endFill();
        app.stage.addChild(blackOverlay);

        // Display the number of remaining lives
        const lifeText = new PIXI.Text(`You Win`, {
            fontSize: 30,
            fill: 0xFFFFFF,
            align: 'center'
        });
        lifeText.x = app.screen.width / 2 - lifeText.width / 2;
        lifeText.y = app.screen.height / 2 - lifeText.height / 2;
        app.stage.addChild(lifeText);

        // Wait for 2 seconds (adjust the duration as needed)
        setTimeout(() => {
            // Remove the black overlay and life text
            app.stage.removeChild(blackOverlay);
            app.stage.removeChild(lifeText);

            // Make the character visible again
            // this.sprite.visible = true;
            // this.sprite.x = 100;
        }, 2000);
    }
}

//clouds

const character = new Character(app, 20, 500);

const knife = new Knife(app);


const keys = {};

// pause---------------------------
let isPaused = false;
// Create a graphics object for the pause overlay
const pauseOverlay = new PIXI.Graphics();
pauseOverlay.beginFill(0x000000, 0.1); // Adjust color and transparency as needed
pauseOverlay.drawRect(0, 0, app.screen.width, app.screen.height);
pauseOverlay.endFill();
pauseOverlay.visible = false; // Initially, the overlay is hidden

// Create a filter for the blur effect
const blurFilter = new PIXI.filters.BlurFilter();
blurFilter.blur = 5; // Adjust the blur amount as needed
pauseOverlay.filters = [blurFilter];
app.stage.addChild(pauseOverlay);
/*--------------------------------------------*/

const finalLevel = 2;

function visibility(enemies, obstacles, platforms, bricks, background, clouds){
    for(let i = 1; i <= finalLevel; i++){
        if(i != level){
            levels[i].background.sprite.visible = false;

            levels[i].platforms.forEach(platform => {
                platform.sprite.visible = false;
            });

            levels[i].clouds.forEach(cloud => {
                cloud.sprite.visible = false;          
            });

            levels[i].obstacles.forEach(obs => {
                obs.sprite.visible = false; 
            });

            levels[i].enemies.forEach(enemy => {
                enemy.sprite.visible = false; 
                enemy.HealthText.visibile = false;
                // console.log(enemy.sprite.x);
            });

            levels[i].bricks.forEach(brick => {
                brick.sprite.visible = false;
            });

            levels[i].collectors.forEach(collect => {
                collect.sprite.visible = false;
            });
        }
        else{
            levels[i].background.sprite.visible = true;

            levels[i].platforms.forEach(platform => {
                platform.sprite.visible = true;
            });

            levels[i].clouds.forEach(cloud => {
                cloud.sprite.visible = true;          
            });

            levels[i].obstacles.forEach(obs => {
                obs.sprite.visible = true; 
            });

            levels[i].enemies.forEach(enemy => {
                enemy.sprite.visible = true; 
                enemy.HealthText.visibile = true;
                // console.log(enemy.sprite.x);
            });

            levels[i].bricks.forEach(brick => {
                brick.sprite.visible = true;
            });

            
            levels[i].collectors.forEach(collect => {
                collect.sprite.visible = true;
            });
        }
    }
}

// try fps reduction
var FPS_setter = 15; // 1000/40 = 25 fps
var times = 0;

//main loop
app.ticker.add((delta) => {
    if(delta > 2){
        delta = 0;
    }
    var timeNow = (new Date()).getTime();
    var timeDiff = timeNow - times;
    if(timeDiff < FPS_setter){
        return;
    }
    times = timeNow;
    
    // console.log(delta)
    if(level > finalLevel){
        change_level();
        return;
    }
    if (isPaused) {
        return; // Exit the function if the game is paused
    }

    if(level <= finalLevel){
        visibility(levels[level].enemies, levels[level].obstacles, levels[level].platforms, 
            levels[level].bricks, levels[level].background, levels[level].clouds);
    }

    if (character.sprite.x > app.screen.width / 2) {
        // Move the background and platforms in the opposite direction of the character
        const movementSpeed = 10; // Adjust the speed as needed
        
        if(character.sprite.x >= levels[level].endLevel && character.starCount >= levels[level].min_stars){
            character.starCount = 0;
            level++;
            character.knifeCount+=3;
            change_level();
            character.sprite.x = levels[level].character_init_position.x;
            character.sprite.y = levels[level].character_init_position.y;
        }

        levels[level].endLevel -= character.run_speed;

        levels[level].background.sprite.x -= character.run_speed/10;
        
        levels[level].platforms.forEach(platform => {
            platform.sprite.x -= character.run_speed;
        });

        levels[level].clouds.forEach(cloud => {
            cloud.sprite.x -= character.run_speed/7;          
        });

        levels[level].obstacles.forEach(obs => {
            obs.sprite.x -= character.run_speed;
        });

        levels[level].enemies.forEach(enemy => {
            enemy.penX -= character.run_speed;
            enemy.sprite.x -= character.run_speed;
            // console.log(enemy.sprite.x);
        })

        levels[level].bricks.forEach(brick => {
            brick.sprite.x -= character.run_speed;
        });

        levels[level].collectors.forEach(collect => {
            collect.sprite.x -= character.run_speed;
        });

        character.sprite.x = app.screen.width / 2;
    }
    // console.log(levels[level].checkpoint, levels[level].endLevel);
    if (character.sprite.x < app.screen.width / 15) {
        // Move the background and platforms in the opposite direction of the character
        const movementSpeed = 10; // Adjust the speed as needed

        levels[level].background.sprite.x += character.run_speed/10;

        levels[level].endLevel += character.run_speed;
        
        levels[level].platforms.forEach(platform => {
            platform.sprite.x += character.run_speed;
        });

        levels[level].clouds.forEach(cloud => {
            cloud.sprite.x += character.run_speed/7;          
        });

        levels[level].obstacles.forEach(obs => {
            obs.sprite.x += character.run_speed;
        });

        levels[level].enemies.forEach(enemy => {
            enemy.penX += character.run_speed;
            enemy.sprite.x += character.run_speed;
            // console.log(enemy.sprite.x);
        })

        levels[level].bricks.forEach(brick => {
            brick.sprite.x += character.run_speed;
        });

        levels[level].collectors.forEach(collect => {
            collect.sprite.x += character.run_speed;
        });

        character.sprite.x = app.screen.width / 15;
    }

    character.update(levels[level].platforms, levels[level].obstacles, levels[level].enemies, levels[level].bricks, levels[level].collectors);
    // for(const knife of knifes){
    //     knife.update(enemies);
    // }
    knife.update(levels[level].enemies);
    //for enimies
    for (const enemy of levels[level].enemies) {
        enemy.update(levels[level].platforms, levels[level].bricks);
    }


    // key presses
    if(keys['x'] || keys['X']){
        character.run_speed = 20;
        character.CurrentAnimation.animationSpeed = 0.6;
    }
    else{
        character.run_speed = 10;
        character.CurrentAnimation.animationSpeed = 0.4;
    }

    if (keys[' '] || keys['ArrowUp']) {
        character.jump();
        if(!character.jumping){
            character.jumping = true;
            character.CurrentAnimation.textures = character.JumpImages;
            character.CurrentAnimation.loop = false;
            character.CurrentAnimation.play();
        }
    }
    
    if(keys['a']){
        // character.throwKnife();
        if(character.knifeCount > 0){
            if(!character.isThrowing){
                character.isThrowing = true;
                character.CurrentAnimation.textures = character.ThrowImages;
                character.CurrentAnimation.loop = false;
                character.CurrentAnimation.play();
            }
        }
    }

    // running, standing
    if (keys['ArrowRight']) {
        character.run_forward();
        if (!character.isRunning) {
            // Set running animation here
            character.CurrentAnimation.textures = character.RunImages;
            character.CurrentAnimation.loop = true;
            character.CurrentAnimation.play();
            character.isRunning = true;
            character.isStanding = false;
        
        }
    } else if (keys['ArrowLeft']) {
        character.run_backward();
        if (!character.isRunning) {
                // Set running animation here
            character.CurrentAnimation.textures = character.RunImages;
            character.CurrentAnimation.loop = true;
            character.CurrentAnimation.play();
            character.isRunning = true;
            character.isStanding = false;
        }
    } else if (!keys['ArrowRight'] && !keys['ArrowLeft']) {
            // If no movement keys are pressed, set the standing animation
        character.CurrentAnimation.textures = character.StandImages;
        character.CurrentAnimation.play();
        character.CurrentAnimation.loop = true;
        character.isRunning = false;
        character.isStanding = true;
    }
    

    // Make sure the animated sprite is being updated
    app.renderer.render(app.stage);
});


// events
document.addEventListener('keydown', (event) => {
    keys[event.key] = true;
    // alert(event.key)

    if (keys['p'] || keys['P']) {
        isPaused = !isPaused;

        if (isPaused) {
            // Show the pause overlay and apply the blur effect
            pauseOverlay.visible = true;
            app.stage.filters = [blurFilter];
        } else {
            // Hide the pause overlay and remove the blur effect
            pauseOverlay.visible = false;
            app.stage.filters = [];
        }
    }
    if (keys['a'] || keys['A']) {
        if(character.knifeCount > 0){
            knife.sprite.x = character.sprite.x;
            knife.sprite.y = character.sprite.y;
    
            character.knifeCount--;
            // knifes.splice(0,1);
    
            // character.throwKnife();
            knife.throwKnife();
        }
    }
});

document.addEventListener('keyup', (event) => {
    keys[event.key] = false;
});
