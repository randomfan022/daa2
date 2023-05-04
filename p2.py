tools:visibility="visible">
 <Button
 android:id="@+id/button"
 android:layout_width="wrap_content"
 android:layout_height="wrap_content"
 android:text="Long Click on Me"
 android:textSize="25sp"
 android:visibility="visible"
 app:layout_constraintBottom_toBottomOf="parent"
 app:layout_constraintLeft_toLeftOf="parent"
 app:layout_constraintRight_toRightOf="parent"
 app:layout_constraintTop_toTopOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>



package com.example.secondprog;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
public class MainActivity extends AppCompatActivity {
 private Button button;
 @Override
 protected void onCreate(Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);
 setContentView(R.layout.activity_main);
 button = findViewById(R.id.button);
 registerForContextMenu(button);
 }
 @Override
 public void onCreateContextMenu(ContextMenu menu, View v, 
ContextMenu.ContextMenuInfo menuInfo) {
 getMenuInflater().inflate(R.menu.menu,menu);
 super.onCreateContextMenu(menu, v, menuInfo);
 }
 @Override
 public boolean onContextItemSelected(@NonNull MenuItem item) {
 Toast.makeText(this, ""+item.getTitle(), Toast.LENGTH_SHORT).show();
 return super.onContextItemSelected(item);
 }
}




<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
 <item
 android:title="@string/one"
 />
 <item
 android:title="@string/two"
 />
 <item
 android:title="@string/three"
 />
 <item
 android:title="@string/four"
 />
 <item
 android:title="@string/five"
 />
</menu>
