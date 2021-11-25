# GLSL

vertex_shader = """
#version 460
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;

out vec3 outColor;
out vec2 outTexCoords;

void main()
{
    vec4 norm = vec4(normal, 0.0);

    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;

    vec4 light = vec4(pointLight, 1.0);

    float intensity = dot(modelMatrix * norm, normalize(light - pos));

    gl_Position = projectionMatrix * viewMatrix * pos;

    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2) * intensity;
    outTexCoords = texCoords;
}
"""

toon_shader_Vertex = """
#version 330 core
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
 
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform mat4 mvpMatrix;
uniform float time;
uniform float silhouetteThickness;
uniform vec3 silhouetteColor;
 
out vec3 fsSilhouetteColor;
out float fsTime;
 
 
void main()
{
    vec4 pos = mvpMatrix * vec4(position.xyz + (normal * silhouetteThickness), 1);
    fsSilhouetteColor = silhouetteColor;
    fsTime = time;
    gl_Position = pos;
}

"""

toon_shader_fragment = """
#version 330 core
out vec4 FragColor;
 
in vec3 fsSilhouetteColor;
in float fsTime;
 
void main()
{
    float t = sin(fsTime * 5.0) * 0.5 + 0.5;
    vec3 baseColor = vec3(0.5, 0.1, 0.0);
    vec3 color = mix(baseColor, fsSilhouetteColor, t);
    FragColor = vec4(color, 1.0f);
}
"""


fragment_shader = """
#version 460
layout (location = 0) out vec4 fragColor;

in vec3 outColor;
in vec2 outTexCoords;

uniform sampler2D tex;

void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""

