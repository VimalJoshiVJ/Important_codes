import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# Molecule names
molecules = ["Coronene", "6OH-Coronene", "3NH$_{\\mathbf{2}}$-Coronene", "6F-Coronene", "6CN-Coronene", "3OH_3F-Coronene", "3OH_3CN-Coronene", "3NH$_{\\mathbf{2}}$_3F-Coronene", "3NH$_{\\mathbf{2}}$_3CN-Coronene"]
# HOMO and LUMO energies (in eV) - replace with your values
HOMO = [-5.611, -4.939, -4.391, -6.148, -7.511, -5.485, -6.132, -5.068, -5.631]
LUMO = [-1.608, -1.126, -0.806, -2.214, -3.901, -1.659, -2.736, -1.469, -2.544]

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
    plt.text(x_shift+0.2, (HOMO[i]+LUMO[i])/2, f"{gaps[i]:.2f}",  va="center", fontsize=11)
       
    # Molecule label at bottom
    plt.text(x_shift, -17, mol, ha="center", fontsize=12, rotation=90, fontweight="bold")
# Remove top, bottom, and right border lines
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["bottom"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
# Axis setup
plt.ylim(-10.5, 1.5)
plt.xlim(-1.5,30)
plt.ylabel("Energy (eV)", fontsize=12)
#plt.title("HOMO–LUMO Energy Levels", fontsize=14, fontweight="bold")
plt.xticks([])
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()
