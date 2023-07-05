#version 330 core
out vec4 FragColor;

in vec3 Normal;  
in vec3 FragPos;  
in vec3 bPos;

uniform vec3 lightPos; 
uniform vec3 viewPos;
uniform vec3 lightColor;
uniform vec3 objectColor;

void main()
{
    vec3 color;
    // ambient
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;

    // diffuse
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    // specular
    float specularStrength = 0.5;
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
    vec3 specular = specularStrength * spec * lightColor;
    float yPos = bPos.y ;

    if (yPos <= 5.0){
    color = vec3(0,0,255)/255;
    }else if (yPos <= 10.0){
    color = vec3(0,255,255)/255;
    }else if (yPos <= 15.0){
    color = vec3(0,255,100)/255;
    }else if (yPos <= 20.0){
    color = vec3(100,255,0)/255;
    }else if (yPos <= 25.0){
    color = vec3(255,255,0)/255;
    }else if (yPos <= 30.0){
    color = vec3(255,100,0)/255;
    }else{
    color = vec3(255,0,0);
    }

    vec3 result = (ambient + diffuse + specular) * color * 1.7;
    FragColor = vec4(result, 1.0);
} 