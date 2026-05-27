import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# Molecule names
molecules = ["Coronene", "6OH-Coronene", "6NH2-Coronene", "6F-Coronene", "6CN-Coronene"]

# HOMO and LUMO energies (in eV) - replace with your values
HOMO = [-5.6074, -4.5729, -4.3871, -6.1444, -7.5091]
LUMO = [-1.5973, -0.7924, -0.7935, -2.202, -3.891]

# HOMO-LUMO gaps
gaps = [LUMO[i] - HOMO[i] for i in range(len(HOMO))]

for i, mol in enumerate(molecules):
    x_shift = i * 3.0  # horizontal spacing
    
    # HOMO line
    plt.hlines(HOMO[i], x_shift-0.5, x_shift+0.5, colors="red", linewidth=2, label="HOMO" if i==0 else "")
    plt.text(x_shift+0.6, HOMO[i], f"{HOMO[i]:.2f}", va="center", fontsize=9)
    
    # LUMO line
    plt.hlines(LUMO[i], x_shift-0.5, x_shift+0.5, colors="black", linewidth=2, label="LUMO" if i==0 else "")
    plt.text(x_shift+0.6, LUMO[i], f"{LUMO[i]:.2f}", va="center", fontsize=9)
    
    # HOMO-LUMO gap arrow
    plt.annotate(
        "", 
        xy=(x_shift, LUMO[i]), 
        xytext=(x_shift, HOMO[i]),
        arrowprops=dict(arrowstyle="<->", linewidth=1.2)
    )
    plt.text(x_shift+0.2, (HOMO[i]+LUMO[i])/2, f"{gaps[i]:.2f}", rotation=90, va="center", fontsize=11)
       
    # Molecule label at bottom
    plt.text(x_shift, -11, mol, ha="center", fontsize=12, fontweight="bold")
# Remove top, bottom, and right border lines
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
# Axis setup
plt.ylim(-8.5, -0.5)
plt.xlim(-1.5,15)
plt.ylabel("Energy (eV)", fontsize=12)
#plt.title("HOMO–LUMO Energy Levels", fontsize=14, fontweight="bold")
plt.xticks([])
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()
